__author__ = 'zoulida'

import tushare as ts


'''
    ts_code  trade_date  turnover_rate     pe
0  000001.SH   20181018           0.38  11.92
1  000300.SH   20181018           0.27  11.17
2  000905.SH   20181018           0.82  18.03
3  399001.SZ   20181018           0.88  17.48
4  399005.SZ   20181018           0.85  21.43
5  399006.SZ   20181018           1.50  29.56
6  399016.SZ   20181018           1.06  18.86
7  399300.SZ   20181018           0.27  11.17
'''

pro = ts.pro_api('69d6b836725cd75df21b39873603b14fed58d101bc033b991b51eb41')

import tools.connectMySQL as CL
cursor, db = CL.getStockDataBaseCursorAndDB()

sqlSentence4 = "SELECT * FROM stockdatabase.stock_index_daily;"
df = pro.index_daily(ts_code='000001.SH',start_date='20190122', end_date=None)

print(df)

from sqlalchemy import create_engine
engine = create_engine('mysql://root:root@127.0.0.1/stockDataBase?charset=utf8')

#¥Ê»Î ˝æ›ø‚
df.to_sql('stock_index_daily',engine,if_exists='append')