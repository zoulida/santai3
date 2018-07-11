import numpy as np
import pandas as pd
import tushare as ts
import datetime
import time
import tushare as ts
import os

data_dir = 'D:\\python_study\\stock_hist_data\\'  # 下载数据的存放路径

# ts.get_sz50s() #获取上证50成份股  返回值为DataFrame：code股票代码 name股票名称

cal_dates = ts.trade_cal()  # 返回交易所日历，类型为DataFrame, calendarDate  isOpen


# 本地实现判断市场开市函数
#@date: str类型日期 eg.'2017-11-23'


def is_open_day(date):
    #print(cal_dates[cal_dates['calendarDate'] == date])
    if date in cal_dates['calendarDate'].values:
        return cal_dates[cal_dates['calendarDate'] == date].iat[0, 1] == 1
    return False

dateend=datetime.date.today()
print(is_open_day(dateend.strftime('%Y-%m-%d')))