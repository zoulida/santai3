__author__ = 'Administrator'

from tools.LogTools import *
logger = Logger(logName='log.txt', logLevel="DEBUG", logger="logTest.py").getlog()

logger.debug("苍井空")
logger.info("麻生希")
logger.warning("小泽玛利亚")
logger.error("桃谷绘里香")
logger.critical("泷泽萝拉")