import socket
import subprocess

serve=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serve.bind(('192.168.12.179',8081))
serve.listen(5)

while True:
    conn,addre=serve.accept()
    print('客户端： '+addre)


