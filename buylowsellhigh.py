import pandas_datareader as data
import pandas as pd
import numpy as np

start_date = "2014-04-01"
end_date = "2021-12-31"

pd.set_option("display.width", 1000)

goog_data = data.DataReader("GOOG","yahoo",start_date, end_date)
# print(goog_data)

goog_data_signal = pd.DataFrame(index = goog_data.index)
goog_data_signal["price"] = goog_data["Adj Close"]
goog_data_signal["daily_difference"] = goog_data_signal["price"].diff()
goog_data_signal["signal"] = 0.0
goog_data_signal["signal"] = np.where(goog_data_signal.daily_difference > 0, 1.0, 0.0)


print(goog_data_signal)
