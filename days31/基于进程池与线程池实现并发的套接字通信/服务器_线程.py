from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',8088))
server.listen(5)

def connect(server):
    while True:
        conn, addr = server.accept()
        print(addr)
        p = ThreadPoolExecutor(2)  # 默认开启的线程数是cpu的核数*5
        p.submit(comunicate, conn)


def comunicate(conn):
    while True:
        try:
            msg = conn.recv(1024).decode('utf-8')
            if not msg: break
            print(msg)
            conn.send(msg.upper().encode('utf-8'))
        except ConnectionResetError:
            break
    conn.close()

if __name__ == '__main__':
    connect(server)

