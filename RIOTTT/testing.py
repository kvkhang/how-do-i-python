import aiohttp
import asyncio
import os
import time
import csv
import json

# Load API Key from .env file


API_KEY = os.getenv("RIOT_API_KEY")

# Riot API Endpoints
MATCH_HISTORY_URL = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?count={count}"
MATCH_DETAILS_URL = "https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}"
MATCH_TIMELINE_URL = (
    "https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline"
)

HEADERS = {"X-Riot-Token": API_KEY}
CSV_FILE = "ranked_solo_timelines.csv"  # File only for ranked solo queue


def init_csv():
    """Initialize CSV file with headers if it doesn't exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["match_id", "timeline_json"])  # CSV Headers


async def fetch(session, url, retries=3):
    """Fetch data from Riot API with retry logic."""
    for attempt in range(retries):
        try:
            async with session.get(url, headers=HEADERS) as response:
                if response.status == 200:
                    return await response.json()
                elif response.status == 429:  # Rate Limited
                    retry_after = int(response.headers.get("Retry-After", 5))
                    print(
                        f"[WARNING] Rate limited. Retrying in {retry_after} seconds..."
                    )
                    await asyncio.sleep(retry_after)
                else:
                    print(f"[ERROR] {response.status} - {url}")
                    return None
        except Exception as e:
            print(f"[ERROR] Exception {e} on {url}")

        print(f"[INFO] Retrying ({attempt + 1}/{retries})...")
        await asyncio.sleep(2)

    return None  # Failed after retries


async def get_ranked_solo_match_ids(session, puuid, count=20):
    """Fetch recent Ranked Solo Queue match IDs for a given PUUID."""
    url = MATCH_HISTORY_URL.format(puuid=puuid, count=count)
    match_ids = await fetch(session, url)

    ranked_solo_matches = []
    for match_id in match_ids:
        match_url = MATCH_DETAILS_URL.format(match_id=match_id)
        match_data = await fetch(session, match_url)

        if (
            match_data and match_data["info"]["queueId"] == 420
        ):  # Ranked Solo Queue only
            ranked_solo_matches.append(match_id)

        await asyncio.sleep(1)  # Prevent spamming requests

    return ranked_solo_matches


async def save_match_timelines(session, match_ids):
    """Fetch timelines for Ranked Solo matches and save them to CSV."""
    existing_match_ids = set()

    # Read existing match IDs from CSV to avoid duplicates
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            existing_match_ids = {row[0] for row in reader}

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        for match_id in match_ids:
            if match_id in existing_match_ids:
                print(f"[INFO] Match {match_id} already in CSV. Skipping...")
                continue

            url = MATCH_TIMELINE_URL.format(match_id=match_id)
            timeline_data = await fetch(session, url)

            if timeline_data:
                writer.writerow([match_id, json.dumps(timeline_data)])
                print(f"[INFO] Saved timeline for Ranked Solo match {match_id}")

            await asyncio.sleep(1)  # Prevent API spam


async def main():
    """Main function to gather Ranked Solo Queue match timelines and save them to CSV."""
    init_csv()  # Ensure CSV file exists
    puuid = "YOUR_PUUID_HERE"  # Replace with your PUUID

    async with aiohttp.ClientSession() as session:
        ranked_solo_match_ids = await get_ranked_solo_match_ids(
            session, puuid, count=10
        )
        print(f"Ranked Solo Match IDs: {ranked_solo_match_ids}")

        if ranked_solo_match_ids:
            await save_match_timelines(session, ranked_solo_match_ids)


# Run the script
asyncio.run(main())
