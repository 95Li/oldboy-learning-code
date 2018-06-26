import time
from socket import  *

client=socket(AF_INET,SOCK_DGRAM)

msg='get new time'
client.sendto(msg.encode('utf-8'),('192.168.12.108',8088))

date,addr=client.recvfrom(1024)
print(date.decode('utf-8'))
