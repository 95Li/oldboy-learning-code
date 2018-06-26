import json
import struct
import os
import hashlib
from socket import *
from days26.FTP import common

client=socket(AF_INET,SOCK_STREAM)
client.connect(('192.168.12.162',8082))
BASE_PATH='F:\python\object\days2\days26\FTP\客户端文件'

while True:
    print('''
    1.Upload
    2.Download    
    ''')

    choice=input('Pleasr choice:').strip()
    #上传
    if choice=='1':
        print(('Please enter file name and file path:'))
        file_name=input('file name:').strip()
        file_path=input('file path:').strip()
        if os.path.exists(file_path):
            file_size =os.path.getsize(file_path)

            # 设置报头
            hander_dic = {
                'operation_type':choice,
                'file_name':file_name,
                'total_size': file_size
            }

            # 发送报头
            common.send_hander_dic(client, hander_dic)
            # 发送真实数据
            common.send_date(client, file_path)
        else:
            print('file path error!!!')

    #下载
    if choice == '2':
        file_name = input('Please enter file name:').strip()
        # 设置报头
        hander_dic = {
            'operation_type': choice,
            'file_name': file_name
        }
        # 发送报头
        common.set_hander_dic(client, hander_dic)

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
        file_path = os.path.join(BASE_PATH, '%s.txt' % hander_dic['file_name'])
        common.get_date_by_size(client, file_path, total_size)

client.close()
