import yfinance as yf # type: ignore
import matplotlib as plot #type: ignore

stock = yf.Ticker("NVDA")

stock = stock.history(period="max")

stock.plot.line(y="Close", use_index=True)
