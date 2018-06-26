from threading import  Event,current_thread,Thread
import time
event=Event()

def check():
    print('%s 正在检测服务是否正常。。。' %current_thread().name)
    time.sleep(5)
    event.set()

def connect():
    count=1
    while not event.is_set():
        if count == 4:
            print('')
