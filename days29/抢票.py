from multiprocessing import  Process,Lock
import time,json,random,os

lock=Lock()
def search():
    print('========%s 查票======' % os.getpid())
    info=json.load(open('test.txt'))
    msg='余票为： %s'%info['count']
    print(msg)

def get(lock):
    lock.acquire()
    print('========%s 抢票======'%os.getpid())
    info = json.load(open('test.txt'))
    time.sleep(random.random())
    if info['count']>0:
        info['count']-=1
        time.sleep(random.random())
        json.dump(info,open('test.txt','w'))
        print('抢票成功')
    else:
        print('票已售完')
    lock.release()

def op(lock):
    search()
    get(lock)

if __name__ == '__main__':
    for i in range(0,50):
        p=Process(target=op,args=(lock,))
        p.start()




