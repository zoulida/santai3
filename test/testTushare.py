__author__ = 'zoulida'
import tushare as ts
import pandas as pd

#data=ts.get_hist_data('000001')
#print(data)

df=ts.get_tick_data('000001', '2019-08-01', pause=0.1, src='tt')
print(df)

dd = ts.get_today_ticks('000300')
#print(dd)
