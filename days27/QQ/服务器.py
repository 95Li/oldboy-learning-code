from socket import *

server=socket(AF_INET,SOCK_DGRAM)
server.bind(('192.168.12.141',8089))

addre_list=[]
while True:
    print(4)
    client_date, client_addr =server.recvfrom(1024)
    addre_list.append(client_addr)
    print(0)
    for addr in addre_list:
        print(addr)
        client_addr=str(client_addr).encode('utf-8')
        server.sendto(client_addr,addr)
        print(1)
        server.sendto(client_date, addr)
        print(2)

print(3)
