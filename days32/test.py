# from threading import Event,current_thread,Thread
# import time
#
# event=Event()
#
# def check():
#     print('%s 正在检测服务是否正常....' %current_thread().name)
#     time.sleep(3)
#     event.set()
#
#
# def connect():
#     print('%s 等待连接...' %current_thread().name)
#     event.clear()
#     event.wait(3)     #括号里的是等待时间，程序想继续运行，除非标志位为True或者超时，此处超时不会报错，是继续执行
#     print('%s 开始连接...' % current_thread().name)
#
# if __name__ == '__main__':
#     t1=Thread(target=connect)
#     t2=Thread(target=connect)
#     t3=Thread(target=connect)
#
#     c1=Thread(target=check)
#
#     t1.start()
#     t2.start()
#     t3.start()
#     c1.start()




import time
def consumer():
    '''任务1:接收数据,处理数据'''
    while True:
        x=yield
        print(x)


def producer():
    '''任务2:生产数据'''
    g=consumer()
    print(type(g))
    print(next(g))
    for i in range(10000000):
        g.send(i)

start=time.time()
#基于yield保存状态,实现两个任务直接来回切换,即并发的效果
#PS:如果每个任务中都加上打印,那么明显地看到两个任务的打印是你一次我一次,即并发执行的.
producer() #1.0202116966247559


stop=time.time()
print(stop-start)