import pandas as pd
import numpy as np
from pandas_datareader import data

start_date = '2014-01-01'
end_date = '2018-01-01'
src_data = 'goog_data.pkl'

try :
    goog = pd.read_pickle(src_data)
    print("File data find .... reading GooG")
except FileNotFoundError :
    print("File Not find... downloading")
    goog = data.DataReader('GOOG', 'yahoo',start_date,end_date)
    goog.to_pickle(src_data)

import statistics as stats

time_period = 20
history = []
sma_values = []

for close_price in goog.Close:
    history.append(close_price)
    if len(history) > time_period:
        del(history[0])
    sma_values.append(stats.mean(history))
    
goog_data = goog.assign(ClosePrice=pd.Series(goog.Close,
index=goog.index))
goog_data = goog_data.assign(Simple20DayMovingAverage=pd.Series(sma_values,
index=goog_data.index))
close_price = goog_data['ClosePrice']
sma = goog_data['Simple20DayMovingAverage']

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Google price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
sma.plot(ax=ax1, color='r', lw=2., legend=True)
plt.show()