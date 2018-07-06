__author__ = 'Administrator'


from sqlalchemy import create_engine
import tushare as ts


import pymysql
pymysql.install_as_MySQLdb()

df = ts.get_tick_data('002312', date='2018-07-05')
print(df)
engine = create_engine('mysql://root:root@127.0.0.1/stockdata0?charset=utf8')

#存入数据库
#df.to_sql('tick_data',engine)


#追加数据到现有表
df.to_sql('tick_data',engine,if_exists='replace')