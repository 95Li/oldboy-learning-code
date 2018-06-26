from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from socket import *


client=socket(AF_INET,SOCK_STREAM)

client.connect(('127.0.0.1',8088))

while True:
    msg=input('input:').strip()
    client.send(msg.encode('utf-8'))
    date=client.recv(1024)
    print(date.decode('utf-8'))
