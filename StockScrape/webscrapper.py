import requests 
from bs4 import BeautifulSoup
import pandas as pd 
  
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'} 

urls = [
    'https://www.investing.com/equities/nike',
    'https://www.investing.com/equities/coca-cola-co',
    'https://www.investing.com/equities/microsoft-corp',
    'https://www.investing.com/equities/3m-co',
    'https://www.investing.com/equities/american-express',
    'https://www.investing.com/equities/amgen-inc',
    'https://www.investing.com/equities/apple-computer-inc',
    'https://www.investing.com/equities/boeing-co',
    'https://www.investing.com/equities/cisco-sys-inc',
    'https://www.investing.com/equities/goldman-sachs-group',
    'https://www.investing.com/equities/ibm',
    'https://www.investing.com/equities/intel-corp',
    'https://www.investing.com/equities/jp-morgan-chase',
    'https://www.investing.com/equities/mcdonalds',
    'https://www.investing.com/equities/salesforce-com',
    'https://www.investing.com/equities/verizon-communications',
    'https://www.investing.com/equities/visa-inc',
    'https://www.investing.com/equities/wal-mart-stores',
    'https://www.investing.com/equities/disney',
    ]
chart = [[""] * 15 for _ in range (len(urls))]

print (chart)
# 0. Companies
# 1. Prices
# 2. Changes
# 3. Previous Close
# 4. Open
# 5. Day's Range
# 6. 52 Week Range
# 7. Volume
# 8. Avg Volume
# 9. Market Cap
# 10. Beta (5Y Monthly)
# 11. PE Ratio (TTM)
# 12. EPS (TTM)
# 13. Forward Dividend & Yield
# 14. 1y Target Est

for i in urls:
    # Make a request to fetch the content of the webpage
    response = requests.get(i)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the webpage content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the company name
        company_element = soup.find('h1', {'mb-2.5 text-left text-xl font-bold leading-7 text-[#232526] md:mb-2 md:text-3xl md:leading-8 rtl:soft-ltr'})
        if company_element:
            company = company_element.text
            chart[i][0] = company
        else:
            company = None
            print("Company name not found.")

        # Extract the price
        price_container = soup.find('div', {'class': 'order-1 flex w-full items-center gap-2 md:order-2 md:w-fit'})
        if price_container:
            price_span = price_container.find_all('span')
            if len(price_span) > 0:
                price = price_span[0].text
                chart[i][1] = price_span[0].text
            else:
                price = None
                print("Price span not found.")
        else:
            price = None
            print("Price container not found.")
        
        # Extract the change
        if price_container and len(price_span) > 2:
            change = price_span[2].text
            chart[i][2] = price_span[2].text
        else:
            change = None
            print("Change not found.")
        
        # Extract the volume
        volume_element = soup.find('dd', {'data-test' : 'volume'})
        if volume_element:
            volume = volume_element.text
            chart[i][7] = volume_element.text
        else:
            volume = None
            print("Volume not found.")
    
        # Print the extracted values
        print('------------------------------')
        print(f"Company: {company}")
        print(f"Price: {price}")
        print(f"Change: {change}")
        print(f"Volume: {volume}")
        
        data = {
        'Price': [price],
        'Change': [change],
        'Volume': [volume]
        }
    
        df = pd.DataFrame(data)
        file_name = 'StockData.xlsx'
        with pd.ExcelWriter(file_name) as writer:
            df.to_excel(writer, index=True, sheet_name=company)
        
        print(f"Data has been written to {file_name}")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
print('------------------------------')

# stock_data = pd.DataFrame({'Company' : companies,
#                            'Price' : prices,
#                            'Change' : changes,
#                            'Volume' : volumes})

# datatoexcel = pd.ExcelWriter('StockData.xlsx')

# stock_data.to_excel(datatoexcel)

# datatoexcel.close()