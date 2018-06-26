import time

from socket import *

server=socket(AF_INET,SOCK_DGRAM)
server.bind(('192.168.12.108',8088))

while True:
    date,addr=server.recvfrom(1024)
    date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

    server.sendto(date.encode('utf-8'),addr)