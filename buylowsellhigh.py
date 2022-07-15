import pandas_datareader as data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start_date = "2020-04-01"
end_date = "2022-12-31"

pd.set_option("display.width", 1000)

goog_data = data.DataReader("GOOG","yahoo",start_date, end_date)
# print(goog_data)

goog_data_signal = pd.DataFrame(index = goog_data.index)
goog_data_signal["price"] = goog_data["Adj Close"]
goog_data_signal["daily_difference"] = goog_data_signal["price"].diff()
goog_data_signal["signal"] = 0.0
goog_data_signal["signal"] = np.where(goog_data_signal.daily_difference > 0, 1.0, 0.0)

goog_data_signal['positions'] = goog_data_signal['signal'].diff()

print(goog_data_signal)

fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel="GOOG PRICE")
goog_data_signal['price'].plot(ax = ax1, color = "r", lw=2)

ax1.plot(goog_data_signal.loc[goog_data_signal.positions == -1.0].index, 
goog_data_signal.price[goog_data_signal.positions == -1.0], 'v', markersize = 4, color = "k")

ax1.plot(goog_data_signal.loc[goog_data_signal.positions == 1.0].index, 
goog_data_signal.price[goog_data_signal.positions == 1.0], "^", markersize = 4, color = "m")

#plt.show()

initial_cap = float (1000.0)

positions = pd.DataFrame(index = goog_data_signal.index).fillna(0.0)
portfolio = pd.DataFrame(index=goog_data_signal.index).fillna(0.0)

positions['GOOG'] = goog_data_signal['signal']

portfolio['position'] = positions.multiply(goog_data_signal['price'], axis = 0)
portfolio['cash'] = initial_cap - (positions.diff().multiply(goog_data_signal['price'], axis = 0)).cumsum()
portfolio['total'] = portfolio['position'] + portfolio['cash']

fig2 = plt.figure()

portfolio.plot()
plt.show()