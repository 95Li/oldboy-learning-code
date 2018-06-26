
from  datetime import *
# import datetime
import time
t1=time.time()
print(t1)
time.sleep(6)
t2=time.time()
# t=t2-t1
# print(t)
# print(time.localtime(t1))
# print(time.localtime(t2-t1).tm_sec)
t2=datetime.fromtimestamp(t2)
t1=datetime.fromtimestamp(t1)
print(t2-t1)
# time.strftime("%Y-%m-%d %H:%M:%S  %p")
# print(time.strftime("%Y-%m-%d %H:%M:%S  %p"))
# print(time.strftime("%Y-%m-%d %X"))
# print(time.localtime())
# print(time.gmtime())
