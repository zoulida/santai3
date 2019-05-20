__author__ = 'zoulida'

import tushare as ts
import pandas as pd

def get_all_stock2():
    stock_info = ts.get_stock_basics()
    stock_info.to_csv("E:\\stock_data\\get_stock_basics.csv", encoding="gbk", index=True)
    normal_stocks = stock_info.loc[:,['name']]
    #print(normal_stocks)
    tms = pd.read_csv('E:\\stock_data\\terminated_stock.csv', dtype=str, encoding="gbk")
    #print(tms)
    #print(list(tms.code))
    #delset = tms.loc[:,['code']]
    ks = normal_stocks.drop(list(tms.code))
    #print(ks)
    return ks