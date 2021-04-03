import pandas as pd
import numpy as np
import tensorflow
import matplotlib.pyplot as plt
import yfinance as yf
import requests

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
    print(ticker_company_list)


def getStockData(symbol):

    ticker = yf.Ticker(symbol)
    print(ticker.info['longName'])
    createDataFrame(ticker)

def createDataFrame(ticker):
    df = pd.DataFrame(ticker.history(period="max")).reset_index()

    trading_days = df['Date'].count()
    training_set = .7 * trading_days
    print(int(training_set))

    companyName = ticker.info['longName']

    showOriginalPlot(df,companyName)

def showOriginalPlot(df, companyName):
    df["Date"]=pd.to_datetime(df.Date,format="%Y-%m-%d")
    df.index=df['Date']
    plt.figure(figsize=(16,8))
    plt.plot(df["Close"],label='Close Price history')
    plt.legend()
    plt.title(companyName)
    plt.show() 

queryByCompany('micros')
getStockData('DIS')