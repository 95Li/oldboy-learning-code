from socket import *
from days31.上传下载 import server_common
from days31.上传下载 import common
from concurrent.futures import ThreadPoolExecutor



mark=None

def accept_hander(conn):
    return  common.accept_hander(conn)

def login(conn, hand_info):
    global mark
    mark= server_common.accept_hander(conn, hand_info)

def register(conn, hand_info):
    server_common.register(conn, hand_info)

def upload(conn, hand_info):
    server_common.upload(conn, hand_info,mark)

def download(conn, hand_info):
    server_common.download(conn, hand_info,mark)


func_dir={
    '1':register,
    '2':login,
    '3':upload,
    '4':download
}
def server(conn):
    print(1)
    hand_info = accept_hander(conn)
    choice=hand_info['operation_type']
    func_dir[choice](conn,hand_info)


if __name__ == '__main__':
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(5)
    while True:
        conn, addre = server.accept()
        print(addre)
        p = ThreadPoolExecutor(2)  # 默认开启的线程数是cpu的核数*5
        p.submit(server, conn)



