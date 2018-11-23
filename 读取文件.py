# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import datetime as dt


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    ymd = date.strftime('%Y-%m-%d')
    print(ymd)
    return"2011-01-28"
dates, opening_prices, highest_prices, lowest_prices, closing_prices = np.loadtxt(
    '../data/aapl.csv',
    delimiter=',', usecols=(1, 3, 4, 5, 6),
    unpack=True, dtype='M8[D],f8,f8,f8,f8', converters={1: dmy2ymd})
