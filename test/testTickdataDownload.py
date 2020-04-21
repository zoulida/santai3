__author__ = 'zoulida'

import tushare as ts
df=ts.get_tick_data(code = '600030',date = '2020-04-09',pause=0.1,src='nt')
print(df)