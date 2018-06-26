import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('192.168.12.179',8081))

client.send('connect'.encode('utf-8'))
client.recv(1024)
