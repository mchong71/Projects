import math
import numpy as np
import matplotlib.pyplot
import scipy.stats
import pandas as pd
from pandas.io.data import DataReader
from datetime import datetime, timedelta

def calcVol(symbol):
    data = DataReader(symbol,  "yahoo", datetime(2012,11,1), datetime(2013,1,1))
    close = data["Adj Close"]

    logprices = np.log(close / close.shift(1))
    return np.sqrt(252*logprices.var())

    return close.std()#*math.sqrt(close.count())/1000

def getPrice(symbol, startDate, endDate):
    data = DataReader(symbol,  "yahoo", startDate, endDate)
    return data["Adj Close"][0]

def ExpectedReturns(option):
    tree, prices = option.BinomialTreeEuropeanCallPrice()
    p = 0.5
    expReturn = []

    probs = [p**4, 4*p**3*(1-p), 6*p**2*(1-p)**2, 4*p*(1-p)**3, p**4]

    for i in range(option.N+1):
        expReturn.append(max((prices[option.N][i]-option.strike)-tree[0][0],-tree[0][0]))
    
    return tree, expReturn, probs, prices
