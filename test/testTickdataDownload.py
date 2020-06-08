__author__ = 'zoulida'

import tushare as ts
df=ts.get_tick_data(code = '600030',date = '2020-01-20',pause=0.1,src='tt')#数据源代码只能输入sn,tt,nt其中之一
print(df)