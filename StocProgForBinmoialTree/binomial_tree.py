import math
import numpy as np
import matplotlib.pyplot
import scipy.stats
import pandas as pd
from pandas.io.data import DataReader
from datetime import datetime, timedelta
 
# S0 = 100.0
# K = 110.0
# r = 0.03
# sigma = 0.1
# T = 0.5
N = 4

def calcVol(symbol):
    data = DataReader(symbol,  "yahoo", datetime(2011,1,1), datetime(2012,1,1))
    close = data["Adj Close"]
    return close.std()*math.sqrt(close.count())/1000

def getPrice(symbol, startDate, endDate):
    data = DataReader(symbol,  "yahoo", startDate, endDate)
    return data["Adj Close"][0]

class Option:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, asset, strike, interest, time):
        self.asset = asset
        self.vol = calcVol(asset)
        self.price = getPrice(asset, datetime(2013,1,1), datetime(2013,1,2))
        self.strike = strike
        self.interest = interest
        self.time = time
    
    def BinomialTreeEuropeanCallPrice(self):
        deltaT = self.time / N
     
        u = math.exp(self.vol * math.sqrt(deltaT))
        d = 1.0 / u
     
        # Initialise our f_{i,j} tree with zeros
        fs = [[0.0 for j in xrange(i + 1)] for i in xrange(N + 1)]
     
        a = math.exp(self.interest * deltaT)
     
        p = (a - d) / (u - d)
        oneMinusP = 1.0 - p
     
        # Compute the leaves, f_{N, j}
        for j in xrange(i+1):
            fs[N][j] = max(self.price * u**j * d**(N - j) - self.strike, 0.0)
     
        for i in xrange(N-1, -1, -1):
            for j in xrange(i + 1):
                fs[i][j] = math.exp(-self.interest * deltaT) * (p * fs[i + 1][j + 1] + oneMinusP * fs[i + 1][j])
        return fs


def ExpectedReturns(option):
    tree = option.BinomialTreeEuropeanCallPrice()
    p = 0.5
    expReturn = []

    probs[p**4, 4*p**3(1-p), 6*p**2(1-p)**2, 4*p(1-p)**3, p**4]

    for i in range(0,len(tree[N])):
        expReturn.append(max((tree[N][i]-option.strike)-tree[0][0],-tree[0][0]))
    
    print tree[0][0]
    print expReturn
    print probs

if __name__ == '__main__':
    aapl = Option("AAPL", 500, 0.03, 30)
    ExpectedReturns(aapl)
