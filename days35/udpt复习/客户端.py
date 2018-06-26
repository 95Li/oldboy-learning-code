import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr=('127.0.0.1',8080)
while True:
    msg=input('===>').strip().encode('utf-8')
    client.sendto(msg,addr)
    msg,addr=client.recvfrom(1024)
    print(msg.decode('utf-8'))


