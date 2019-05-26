__author__ = 'zoulida'

from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
db = conn.mydb  #连接mydb数据库，没有则自动创建

def getConnectionWuDuJi():
    return db.WuDuJi