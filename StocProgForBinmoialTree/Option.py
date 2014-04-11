import binomial_tree as bt
from datetime import datetime, timedelta
import math
import numpy as np
from datetime import datetime, timedelta

class Option:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, asset, strike, interest, time, N):
        self.asset = asset
        self.vol = bt.calcVol(asset)
        self.price = bt.getPrice(asset, datetime(2013,1,1), datetime(2013,1,2))
        self.strike = strike
        self.interest = interest
        self.time = time
        self.N = N
    
    def BinomialTreeEuropeanCallPrice(self):
        fs = [[0.0 for j in xrange(i + 1)] for i in xrange(self.N + 1)]
        prices = [[0.0 for j in xrange(i + 1)] for i in xrange(self.N + 1)]

        h = self.time/self.N
        u = math.exp((self.interest-0.5*self.vol**2)*h+self.vol*np.sqrt(h))
        d = math.exp((self.interest-0.5*self.vol**2)*h-self.vol*np.sqrt(h))
        drift = math.exp(self.interest*h)
        q = (drift-d)/(u-d)

        prices[0][0] = self.price
        for i in range(1,self.N+1):
            prices[i][0] = prices[i-1][0]*u
            for j in range(1, i+1):
                prices[i][j] = prices[i-1][j-1]*d

        for j in xrange(i+1):
            fs[self.N][j] = max(self.price * u**j * d**(self.N - j) - self.strike, 0.0)
     
        for j in range(self.N+1):
            fs[self.N][j] = max(0,1*(prices[self.N][j]-self.strike))
        for m in range(self.N):
            i = self.N-m-1
            for j in range(i+1):
                fs[i][j] = (q*fs[i+1][j]+(1-q)*fs[i+1][j+1])/drift

        return fs, prices

    # def BinomialTreeEuropeanCallPrice(self):
    #     deltaT = self.time / self.N
     
    #     u = math.exp(self.vol * math.sqrt(deltaT))
    #     print u
    #     d = 1.0 / u
     
    #     # Initialise our f_{i,j} tree with zeros
    #     fs = [[0.0 for j in xrange(i + 1)] for i in xrange(self.N + 1)]
    #     prices = [[0.0 for j in xrange(i + 1)] for i in xrange(self.N + 1)]
     
    #     a = math.exp(self.interest * deltaT)
     
    #     p = 0.5#(a - d) / (u - d)
    #     oneMinusP = 1.0 - p
     
    #     # Compute the leaves, f_{N, j}
    #     for j in xrange(i+1):
    #         fs[self.N][j] = max(self.price * u**j * d**(self.N - j) - self.strike, 0.0)
     
    #     for i in xrange(self.N-1, -1, -1):
    #         for j in xrange(i + 1):
    #             fs[i][j] = math.exp(-self.interest * deltaT) * (p * fs[i + 1][j + 1] + oneMinusP * fs[i + 1][j])
    #     return fs