import pandas as pd
import yfinance as yf

# Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max

def stock_info(stock):
    x = yf.Ticker(stock)
    risk = x.history(period='10y', interval='1mo')['Close'].pct_change().std()
    return_ = x.history(period='10y', interval='1mo')['Close'].pct_change().mean()

    try:
        beta = x.info['beta']
    except:
        beta = float("NAN")

    try:
        debtToEquity = x.info['debtToEquity']
    except:
        debtToEquity = float("NAN")

    try:
        grossMargins = x.info['grossMargins']
    except:
        grossMargins = float("NAN")

    try:
        ebitdaMargins = x.info['ebitdaMargins']
    except:
        ebitdaMargins = float("NAN")

    try:
        operatingMargins = x.info['operatingMargins']
    except:
        operatingMargins = float("NAN")

    return [risk, return_, beta, debtToEquity, grossMargins, ebitdaMargins, operatingMargins]


stock_list = pd.read_csv("bse500_yf.csv")
stock_list = stock_list[:10]

x = stock_list['symbol'].apply(lambda x: stock_info(x))
stock_list[['risk', 'return', 'beta', 'debtToEquity', 'grossMargins', 'ebitdaMargins', 'operatingMargins']] = list(x)
stock_list.to_csv('bse500.csv', index=False)
