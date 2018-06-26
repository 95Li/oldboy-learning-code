import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',8080))

while True:
    res,addr=server.recvfrom(1024)
    res=res.decode('utf-8').upper()
    server.sendto(res.encode('utf-8'),addr)


