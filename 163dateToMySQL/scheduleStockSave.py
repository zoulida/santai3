import datetime
import schedule #pip install schedule
import threading
import time


def job1():
    print("I'm working for job1")
    time.sleep(2)
    print("job1:", datetime.datetime.now())
    import toCVSdef
    toCVSdef.main()




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

            now = datetime.datetime.now()

            # 到达设定时间，结束内循环

            if now.hour == 0 and now.minute == 5:
                break

            # 不到时间就等20秒之后再次检测
            print("Wait for running at 00:05 every day." )
            time.sleep(20)

        job1_task()

def main():
    #job1_task()
    run()

main()