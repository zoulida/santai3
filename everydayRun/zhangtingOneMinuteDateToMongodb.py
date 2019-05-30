__author__ = 'zoulida'


import re
#import time

#from send_mail import sender_139
#import datetime
from data163ToMySQL import wenduj3

from tools.LogTools import *
logger = Logger(logName='log.txt', logLevel="DEBUG", logger="santai3").getlog()

class ZhangtingDietingData:#存储温度计数据，每分钟都有更新：1）下载；2）toJson; 3) 存数据库
    def __init__(self):
        self.strContent = 'var min={"time":"2019-05-27 15:18:48","Data":[[925,6,6,["预盈预增","新股","基金重仓股","抗抑郁"]]]}'

    def getResult(self):
        # 涨跌停1分钟数据统计
        zdt1fzsjtj = 'http://homeflashdata2.jrj.com.cn/limitStatistic/min_and_concept.js'
        zdtObject = wenduj3.GetZDT()
        zdt1fzsjtj_content = zdtObject.getdata(zdt1fzsjtj, headers=zdtObject.header_zdt)
        #logger.info('zdt1fzsjtj Content' + zdt1fzsjtj_content)

        self.strContent = zdt1fzsjtj_content
        p = re.compile(r'{[\w\W]*}', )
        if len(self.strContent) <= 0:
            logger.info('Content\'s length is 0')
            exit(0)
        result = p.findall(self.strContent)
        #print(result[0])
        return result[0]

    def toJson(self, str):
        import json
        params = json.loads(str)
        return params

    def toMongodbTestOk(self, jsonObject):
        from tools.mongodbFactory import getConnectionWuDuJi
        wendujiMongodb = getConnectionWuDuJi()
        wendujiMongodb.insert(jsonObject)
        for i in wendujiMongodb.find():
            print(i)

    def toMongodb(self, jsonObject):
        from tools import mongodbFactory
        wendujiMongodb = mongodbFactory.getConnectionWuDuJi()
        client = mongodbFactory.getClient()

        #wendujiMongodb.insert(jsonObject)

        criteriaObj = {"MetaName":"timestamp"}
        maxTime = {"$set":{"MetaName":"timestamp","maxTime": 666666}}
        #wendujiMongodb.update(criteria = criteriaObj ,document = maxTime, upsert = True, multi = False)
        #wendujiMongodb.update(criteriaObj, maxTime, upsert = True)#亲测可用
        wendujiMongodb.update_one(criteriaObj, maxTime, upsert=True)#只找一个，效率高，在不建索引的前题下
        # with client.start_session() as s:#使用事务
        #     s.start_transaction()
        #     wendujiMongodb.insert_one(jsonObject, session=s)
        #     maxTime = {"maxTime" : 3333333}
        #     wendujiMongodb.upsert(maxTime, upsert = True)
        #
        #     s.commit_transaction()
        for i in wendujiMongodb.find():
            print(i)

    def allTask(self):
        str = self.getResult()
        jsonO = self.toJson(str)
        self.toMongodb(jsonO)

    def getResultTest(self):
        # 涨跌停1分钟数据统计
        zdt1fzsjtj = 'http://homeflashdata2.jrj.com.cn/limitStatistic/min_and_concept.js'
        #zdt1fzsjtj_content = self.getdata(zdt1fzsjtj, headers=self.header_zdt)
        #logger.info('zdt1fzsjtj Content' + zdt1fzsjtj_content)
        p = re.compile(r'{[\w\W]*}', )
        if len(self.strContent) <= 0:
            logger.info('Content\'s length is 0')
            exit(0)
        result = p.findall(self.strContent)
        print(result[0])

        import json
        params = json.loads(result[0])
        print(params)
        print(params['Data'][0][0])
        #print(params['Data'][0][3][0])

        #str = '{"params":{"id":222,"offset":0},"nodename":"topic"}'
        #print(str)
        # params = json.loads(str)
        # print(params['params']['id'])


if __name__ == '__main__':
    logger.info("zhangtingOneMinuteDateToMongodb.py start")
    obj = ZhangtingDietingData()
    obj.allTask()
    #obj.getResultTest()