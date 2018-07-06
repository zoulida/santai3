__author__ = 'Administrator'

from sqlalchemy import create_engine

engine = create_engine('mysql://root:root@127.0.0.1/stockdata0?charset=utf8')

#存入数据库
#df.to_sql('tick_data',engine)



df =[fda,da,fdsa]
#追加数据到现有表
df.to_sql('tick_data',engine,if_exists='append')