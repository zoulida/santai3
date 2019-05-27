__author__ = 'zoulida'


import re
import time
import xlrd
import xlwt
import sys
import os
#import setting
#from setting import is_holiday, DATA_PATH
import pandas as pd
import tushare as ts
#from setting import llogger
import requests
#from send_mail import sender_139
import datetime
from tools.LogTools import *
logger = Logger(logName='log.txt', logLevel="DEBUG", logger="santai3").getlog()

class ZhangtingDietingData:
    def __init__(self):
        self.strtest = 'var min={"time":"2019-05-27 15:18:48","Data":[[925,6,6,["预盈预增","新股","基金重仓股","抗抑郁"]]]}'

    def getResult(self):
        # 涨跌停1分钟数据统计
        zdt1fzsjtj = 'http://homeflashdata2.jrj.com.cn/limitStatistic/min_and_concept.js'
        #zdt1fzsjtj_content = self.getdata(zdt1fzsjtj, headers=self.header_zdt)
        #logger.info('zdt1fzsjtj Content' + zdt1fzsjtj_content)
        p = re.compile(r'{[\w\W]*}', )
        if len(self.strtest) <= 0:
            logger.info('Content\'s length is 0')
            exit(0)
        result = p.findall(self.strtest)
        print(result[0])

        import json
        params = json.loads(result[0])
        print(params)

        #str = '{"params":{"id":222,"offset":0},"nodename":"topic"}'
        #print(str)
        # params = json.loads(str)
        # print(params['params']['id'])


if __name__ == '__main__':
    logger.info("start")
    obj = ZhangtingDietingData()
    obj.getResult()