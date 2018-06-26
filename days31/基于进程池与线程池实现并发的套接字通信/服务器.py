from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from socket import *


server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)
# server.setsockopt(SOL_SOCKET,SO_REUSEPORT, 1)


def comunicate(conn):
    while True:
       try:
           msg= conn.recv(1024).decode('utf-8')
           if not msg: break
           print(msg)
           conn.send(msg.upper().encode('utf-8'))

       except ConnectionResetError:
           break

    conn.close()

def connect(server):
    # server = socket(AF_INET, SOCK_STREAM)
    # server.bind(('127.0.0.1', 8080))
    # server.listen(5)

    while True:
        conn,address=server.accept()
        p = ProcessPoolExecutor()  # 默认开启的进程数是cpu的核数
        p.submit(comunicate,conn)

if __name__ == '__main__':
    connect(server)



