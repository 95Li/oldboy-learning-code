import  time
from threading import Thread,current_thread,active_count,enumerate

def run():
    print(current_thread().name)
    time.sleep(3)

if __name__ == '__main__':
    t1=Thread(target=run,name='first')
    t2=Thread(target=run,name='two')

    t1.start()
    t2.start()
    print(active_count())
    print(enumerate())
    print(current_thread().name)
