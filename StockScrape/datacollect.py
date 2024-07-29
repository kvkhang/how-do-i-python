import yfinance as yf  # type: ignore
import matplotlib as plot  # type: ignore

stock = yf.Ticker("NVDA")

stock = stock.history(period="max")

stock.plot.line(y="Close", use_index=True)

del stock["Dividends"]
del stock["Stock Splits"]

stock["Tomorrow"] = stock["Close"].shift(-1)
stock["Target"] = (stock["Tomorrow"] > stock["Close"]).astype(int)
stock = stock.loc["1990-01-01":].copy()

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, min_samples_split=100, random_state=1)

train = stock.iloc[:-100]
test = stock.iloc[-100]

predictors = ["Close", "Volume", "Open", "High", "Low"]
model.fit(train[predictors], train["Target"])

from sklearn.metrics import precision_score

preds = model.predict(test[predictors].values.reshape(-1, 1))
preds
