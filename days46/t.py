import time
import sys
t = 30

while not t == 0:
    t -= 1
    print('\r %s' %t, end='',flush=True)
    time.sleep(1)
