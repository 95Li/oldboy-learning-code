from multiprocessing import Process
import time

x=1000

def task():
    global x
    x=1
    print(x)

if __name__ == '__main__':
    p=Process(target=task)
    p.start()
    print(x)

print(x)