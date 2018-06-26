from multiprocessing import Process
import time
import os

x=1000

def task():
    global x
    print('ziid :%s   zhuid:   %s'%(os.getpid(),os.getppid()))
    x=1
    print('zi',x)

if __name__ == '__main__':
    p=Process(target=task)
    p.start()

    p.join()

    p.terminate()
    print(p.is_alive())

    print(os.getpid(),'=======',os.getppid())


    print('zhu',x)

