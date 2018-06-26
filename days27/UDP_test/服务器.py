import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',8088))

while True:
    client_date,client_addr=server.recvfrom(1024)
    server.sendto(client_date.upper(),client_addr)