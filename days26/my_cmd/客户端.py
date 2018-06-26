import json
import struct
import hashlib
from socket import *


client=socket(AF_INET,SOCK_STREAM)
client.connect(('192.168.12.108',8083))

while True:
    cmd=input('==>:').strip()
    client.send(cmd.encode('utf-8'))

    #接收报头长度
    hander_size=struct.unpack('i',client.recv(4))[0]

    #接收报头内容
    hander_bytes=client.recv(hander_size)

    #解析报头内容
    hander_json=hander_bytes.decode('utf-8')
    hander_dic=json.loads(hander_json)
    print(hander_dic)

    total_size=hander_dic['total_size']

    #根据size获取文件内容
    recv_size=0
    res=b''
    while recv_size<total_size:
        recv_date=client.recv(1024)
        res+=recv_date
        recv_size+=len(recv_date)


    # 判断 传输信息是否正确
    m=hashlib.md5()
    m.update(res)
    if hander_dic['md5']==m.hexdigest():
        print(res.decode('gbk'))
    else:
        print('传输错误')


client.close()















