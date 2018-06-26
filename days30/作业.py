from threading import Thread,Lock
lock=Lock
count=0
def task():
    global count
    count+=1

if __name__ == '__main__':
    for i in range(4):
        t=Thread(target=task)
        t.start()
    print(count)


