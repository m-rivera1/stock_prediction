import pandas as pd
import numpy as np
import tensorflow
# import matplotlib.pyplot as plt
import yfinance as yf
import requests
import json
import datetime as dt

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 20, 10
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics


def queryByCompany(searchparam):
    ticker_company_list = []
    ticker_list = []
    url = f"http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={searchparam}&region=1&lang=en"
    results = requests.get(url).json()
    for x in results['ResultSet']['Result']:
        ticker_company_list.append(x['name'])
        ticker_list.append(x['symbol'])


def getStockData(symbol):

    ticker = yf.Ticker(symbol)
    return ticker


def createDataFrame(ticker):
    df = pd.DataFrame(ticker.history(period="5y")).reset_index()
    return df


def getStockDates(ticker):
    t = getStockData(ticker)
    df = createDataFrame(t)
    df["Date"] = pd.to_datetime(df.Date, format="%Y-%m-%d")
    dates = df.Date.apply(lambda x: x.strftime("%Y-%m-%d"))

    data = dates.to_list()

    return data


def getStockClose(ticker):
    t = getStockData(ticker)
    df = createDataFrame(t)
    close = df['Close'].to_list()

    return close


def getCompanyName(ticker):
    t = getStockData(ticker)
    cName = t.info['longName']

    return cName


# getStockData('DIS')