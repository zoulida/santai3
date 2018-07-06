__author__ = 'Administrator'
import tushare as ts
data=ts.get_hist_data('300274')
print(data)