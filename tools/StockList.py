__author__ = 'zoulida'

import tushare as ts
import pandas as pd
from tools.LogTools import Logger
logger = Logger(logName='log.txt', logLevel="DEBUG", logger="logTest.py").getlog()
def get_all_stock2():

    stock_info = ts.get_stock_basics()
    stock_info.to_csv("E:\\stock_data\\get_stock_basics.csv", encoding="gbk", index=True)
    normal_stocks = stock_info.loc[:,['name']]
    #print(normal_stocks)
    tms = pd.read_csv('E:\\stock_data\\terminated_stock.csv', dtype=str, encoding="gbk")
    #print(tms)
    #print(list(tms.code))
    #delset = tms.loc[:,['code']]
    try:
        ks = normal_stocks.drop(list(tms.code))
    except Exception as e:
        import traceback
        print('traceback.print_exc():', traceback.print_exc())
        logger.info(e)
    finally:
        ks = normal_stocks

    print(ks)
    return ks