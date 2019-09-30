__author__ = 'zoulida'
import tushare as ts
import pandas as pd

#data=ts.get_hist_data('000001')
#print(data)

#df=ts.get_tick_data('000001', '2019-08-01', pause=0.1, src='tt')
#print(df)

#dd = ts.get_today_ticks('000300')
#print(dd)

d2 = ts.get_hist_data('hs300', ktype='5') #不要用加日期，加了也是350行。跟踪代码可知是ifeng.com的数据。
print(d2)
