from threading import Thread,Lock
import time

lock=Lock()
x=100

def task():
    global x
    lock.acquire()
    temp=x
    time.sleep(0.1)
    x=temp-10
    lock.release()

if __name__ == '__main__':
    start=time.time()
    t_1=[]
    for i in range(10):
        t=Thread(target=task())
        t_1.append(t)
        t.start()
    # for i in t_1:
    #     t.join()
    print('zhu',x)
    print(time.time()-start)