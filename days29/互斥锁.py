import random
import time
from multiprocessing import  Process

def task1():
    print('name1: egon')
    time.sleep(random.randint(0,3))
    print('sex1:male')
    time.sleep(random.randint(0, 3))
    print('age1:19')

def task2():
    print('name2: egon')
    time.sleep(random.randint(0,3))
    print('sex2:male')
    time.sleep(random.randint(0, 3))
    print('age2:19')

def task3():
    print('name3: egon')
    time.sleep(random.randint(0,3))
    print('sex3:male')
    time.sleep(random.randint(0, 3))
    print('age3:19')

if __name__ == '__main__':
    p1=Process(target=task1)
    p2 = Process(target=task2)
    p3 = Process(target=task3)

    p1.daemon()   #将p设置为主进程的守护进程，主进程结束，无论子进程是否正常执行完，都跟主进程一起结束

    p1.start()
    # p1.join()
    p2.start()
    # p2.join()
    p3.start()
    # p3.join()














