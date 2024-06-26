import yfinance as yf # type: ignore

stock = yf.Ticker("NVDA")

stock = stock.history(period="max")
