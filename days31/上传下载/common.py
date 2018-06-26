import json
import struct
import hashlib

def my_md5(info):
    m = hashlib.md5()
    m.update(info.encode('utf-8'))
    return m.hexdigest()

def check_login(conn,mark):
    conn.send(mark.encode('utf-8'))
    res=conn.recv(1024)
    return res


def accept_hander(conn):
    # try:
        hander_size = struct.unpack('i', conn.recv(4))[0]
        # 接收报头内容
        hander_bytes = conn.recv(hander_size)
        # 解析报头内容
        hander_json = hander_bytes.decode('utf-8')
        hander_dic = json.loads(hander_json)

        print(hander_dic)
        return hander_dic
    # except ConnectionResetError:
    #     return False


def send_hander_dic(conn,hander_dic):
    hander_json = json.dumps(hander_dic)
    hander_bytes = hander_json.encode('utf-8')
    # 发送报头的长度
    hander_size = len(hander_bytes)
    conn.send(struct.pack('i', hander_size))
    # 发送报头、
    conn.send(hander_bytes)

# 发送 文件 内容
def send_date(conn,file_path):
    f = open(file_path, 'rb')
    while True:
        line = f.readline()
        if line:
            conn.send(line)
        else:
            break
    f.close()

def get_date_by_size(conn,file_path,total_size):
    # 根据size获取文件内容
    f = open(file_path, 'a', encoding='utf-8')
    recv_size = 0
    while recv_size < total_size:
        recv_date = conn.recv(1024)
        recv_size += len(recv_date)
        f.write(recv_date.decode('utf-8'))
    f.close()