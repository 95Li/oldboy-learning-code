from socket import *
import time
from multiprocessing import Process

client=socket(AF_INET,SOCK_DGRAM)

def myrecv(msg):
    client.sendto(msg.encode('utf-8'),('192.168.12.141',8089))
    while True:

        server_addr_date,server_addr=client.recvfrom(1024)
        server_date,server_addr=client.recvfrom(1024)
        # if not server_date and server_addr:
        #     break
        print(server_addr_date.decode('utf-8'))
        print(server_date.decode('utf-8'))
        time.sleep(3)
if __name__ == '__main__':
    msg=input('your name :').strip()
    p2=Process(target=myrecv,args=(msg,))
    p2.start()

    while True:
        msg=input('===>').strip()
        client.sendto(msg.encode('utf-8'),('192.168.12.108',8088))
        time.sleep(3)
