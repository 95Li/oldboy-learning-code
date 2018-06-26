import socket

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8080))

while True:
    res=input('speck:    ')
    phone.send(res.encode('utf-8'))
    msg=phone.recv(1024)
    print(msg.decode('utf-8'))

phone.close()
