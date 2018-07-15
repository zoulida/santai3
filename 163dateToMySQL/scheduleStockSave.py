import datetime
import schedule #pip install schedule
import threading
import time

#前置必备代码
import sys
import os
print( "当前工作路径",os.getcwd())
sys.path.append(os.getcwd())
#print(sys.path)



def job1():
    print("I'm working for job1")
    time.sleep(2)
    print("job1:", datetime.datetime.now())
    import toCSVdef
    toCSVdef.main()




def job2():
    print("I'm working for job2")
    time.sleep(2)
    print("job2:", datetime.datetime.now())


def job1_task():
    threading.Thread(target=job1).start()


def job2_task():
    threading.Thread(target=job2).start()


def run():

    #schedule.every(10).seconds.do(job1_task)
    #schedule.every(10).seconds.do(job2_task)


    while True:
        #schedule.run_pending()
        #time.sleep(1)

        while True:
            # 不到时间就等20秒之后再次检测
            time.sleep(5)
            now = datetime.datetime.now()

            # 到达设定时间，结束内循环
            h = 0
            m = 9
            if now.hour == h and now.minute == m:

                break


            print("Wait for running at ", h, ':', m, " every day." )


        job1_task()
        time.sleep(60)

def main():
    #job1_task()
    run() #

main()