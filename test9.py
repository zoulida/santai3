import tushare as ts

df=ts.get_hist_data('600848')
print(df)

df = ts.get_realtime_quotes('000581') #Single stock symbol
df[['code','name','price','bid','ask','volume','amount','time']]

df = ts.get_tick_data('600848',date='2014-01-09')
df.head(10)

