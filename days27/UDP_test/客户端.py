import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg=input('==>').strip()
    client.sendto(msg.encode('utf-8'),('127.0.0.1',8088))
    res,server_addr=client.recvfrom(1024)
    print(res.decode('utf-8'))