from multiprocessing import Process
import time

# def task(name):
#     print('%s is runing'%name)
#     time.sleep(3)
#     print('%s is del' % name)

# if __name__ == '__main__':
#     p=Process(target=task,args=('egin',))
#     p.start()
#     time.sleep(1)
#     print('zhu....')

class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print('%s is runing' % self.name)
        time.sleep(3)
        print('%s is del' % self.name)

if __name__ == '__main__':
    m=MyProcess('egin')
    m.start()

