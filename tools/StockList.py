__author__ = 'zoulida'

import tushare as ts
import pandas as pd
from tools.LogTools import Logger #注意可以.LogTools import Logger相对路径更为简洁一些
from memory_profiler import profile

logger = Logger(logName='log.txt', logLevel="DEBUG", logger="logTest.py").getlog()

@profile
def get_all_stock2():
    import tools.platformPrint as pp
    import tools.mkdir as mkdir
    if pp.UsePlatform() == "Linux":
        mkdir.mkdirA('/volume/stock_data')
        filepath = '/volume/stock_data/get_stock_basics.csv'
    elif pp.UsePlatform() == "Windows":
        mkdir.mkdirA('E:\\stock_data\\')
        filepath = 'E:\\stock_data\\get_stock_basics.csv'

    stock_info = ts.get_stock_basics()
    stock_info.to_csv(filepath, encoding="gbk", index=True)#获得股票列表，一读一写是为了防止网络问题
    normal_stocks = stock_info.loc[:,['name']]
    #print(normal_stocks)
    tms = pd.read_csv(filepath, dtype=str, encoding="gbk")
    #tms2 = pd.read_csv(filepath, dtype=str, encoding="gbk")
    #del tms2
    #tms3 = pd.read_csv(filepath, dtype=str, encoding="gbk")
    #del tms3

    #del pd
    #print(tms)
    #print(list(tms.code))
    #delset = tms.loc[:,['code']]
    try:
        normal_stocks.drop(list(tms.code))
    except Exception as e:
        import traceback
        print('traceback.print_exc():', traceback.print_exc())
        logger.info(e)
    finally:
        ks = normal_stocks
    #del pd
    #print(ks)

    del stock_info, normal_stocks, tms
    import gc
    gc.collect()
    return ks

#@profile
def test():
    print('333333333333333333333333333333333')
    get_all_stock2()
    print('333333333333333333333333333333333')

if __name__ == '__main__':
    get_all_stock2()
    print(get_all_stock2())
    get_all_stock2()
    print('===================================================')
    get_all_stock2()
    print('===================================================')
    get_all_stock2()
