__author__ = 'zoulida'

import tushare as ts
import pandas as pd
from tools.tusharePro import getPro
from tools.LogTools import Logger #注意可以.LogTools import Logger相对路径更为简洁一些
from memory_profiler import profile

logger = Logger(logName='log.txt', logLevel="DEBUG", logger="logTest.py").getlog()

#@profile
def get_all_stock2():
    import tools.platformPrint as pp
    import tools.mkdir as mkdir
    if pp.UsePlatform() == "Linux":
        mkdir.mkdirA('/volume/stock_data')
        filepath = '/volume/stock_data/get_stock_basics.csv'
    elif pp.UsePlatform() == "Windows":
        mkdir.mkdirA('E:\\stock_data\\')
        filepath = 'E:\\stock_data\\get_stock_basics.csv'

    try:
        pro = getPro()
        stock_info = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
        stock_info.to_csv(filepath, encoding="gbk", index=True)#获得股票列表，一读一写是为了防止网络问题
    except Exception as e:
        import traceback
        print('网络获取list错误，从磁盘获取吧。traceback.print_exc():', traceback.print_exc())
        logger.info(e)
        stock_info = pd.read_csv(filepath, dtype=str, encoding="gbk")


    normal_stocks = stock_info.loc[:,['symbol','name']]
    #print(normal_stocks)

    #tms2 = pd.read_csv(filepath, dtype=str, encoding="gbk")
    #del tms2
    #tms3 = pd.read_csv(filepath, dtype=str, encoding="gbk")
    #del tms3

    #del pd
    #print(tms)
    #print(list(tms.code))
    #delset = tms.loc[:,['code']]
    try:
        #normal_stocks.drop(list(tms.code))
        print('############################')
    except Exception as e:
        import traceback
        print('traceback.print_exc():', traceback.print_exc())
        logger.info(e)
    finally:
        ks = normal_stocks
    #del pd
    #print(ks)

    del stock_info, normal_stocks#, tms
    import gc
    gc.collect()
    return ks
'''    symbol     name
0     000001     平安银行
1     000002      万科A
2     000004     国华网安
3     000005     ST星源'''

#@profile
def test():
    print('333333333333333333333333333333333')
    from tusharePro import getPro
    #get_all_stock2()
    pro = getPro()

    #查询当前所有正常上市交易的股票列表

    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    print(data)
    '''  ts_code  symbol     name area industry list_date
0     000001.SZ  000001     平安银行   深圳       银行  19910403
1     000002.SZ  000002      万科A   深圳     全国地产  19910129
2     000004.SZ  000004     国华网安   深圳     软件服务  19910114
3     000005.SZ  000005     ST星源   深圳     环境保护  19901210
4     000006.SZ  000006     深振业A   深圳     区域地产  19920427'''
    print('333333333333333333333333333333333')

if __name__ == '__main__':
    #test()
    '''get_all_stock2()
    print(get_all_stock2())
    get_all_stock2()
    print('===================================================')
    get_all_stock2()
    print('===================================================')
    get_all_stock2()'''
    print(get_all_stock2())
