import pymysql


# 数据库名称和密码
name = 'root'
password = 'root'  # 替换为自己的账户名和密码
# 建立本地数据库连接(需要先开启数据库服务)
db = pymysql.connect('localhost', name, password, charset='utf8')

def getTickCursor():
    ##########################将股票数据存入数据库###########################

    cursor = db.cursor()
    # 创建数据库stockDataBase
    sqlSentence1 = "create database TickData"
    try:
        cursor.execute(sqlSentence1)  # 选择使用当前数据库
    except:
        print("数据库已经存在，无法再次创建");
    sqlSentence2 = "use TickData;"
    cursor.execute(sqlSentence2)
    return cursor

def getStockDataBaseCursor():
    ##########################将股票数据存入数据库###########################


    # 建立本地数据库连接(需要先开启数据库服务)
    #db = pymysql.connect('localhost', name, password, charset='utf8')
    cursor = db.cursor()
    # 创建数据库stockDataBase
    sqlSentence1 = "create database stockDataBase"
    try:
        cursor.execute(sqlSentence1)  # 选择使用当前数据库
    except:
        print("数据库已经存在，无法再次创建");
    sqlSentence2 = "use stockDataBase;"
    cursor.execute(sqlSentence2)
    return cursor