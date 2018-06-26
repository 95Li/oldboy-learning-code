import json
import struct
import os
from days26.FTP import common
from socket import *

server=socket(AF_INET,SOCK_STREAM)
server.bind(('192.168.12.162',8082))
server.listen(5)

BASE_PATH='F:\python\object\days2\days26\FTP\服务器端文件'

while True:
    conn, addre = server.accept()
    print(addre)
    while True:
        try:
            hander_size = struct.unpack('i', conn.recv(4))[0]

            # 接收报头内容
            hander_bytes = conn.recv(hander_size)

            # 解析报头内容
            hander_json = hander_bytes.decode('utf-8')
            hander_dic = json.loads(hander_json)
            print(hander_dic)

            # 1上传  2下载
            if hander_dic['operation_type']=='1':
                total_size = hander_dic['total_size']

                # 根据size获取文件内容
                file_path=os.path.join(BASE_PATH,'%s.txt'%hander_dic['file_name'])
                common.get_date_by_size(conn, file_path, total_size)

            # 1上传  2下载
            if hander_dic['operation_type'] == '2':
                file_path=os.path.join(BASE_PATH,'%s.txt'%hander_dic['file_name'])
                if os.path.exists(file_path):
                    file_size = os.path.getsize(file_path)
                    #设置报头
                    hander_dic = {
                        'operation_type': '2',
                        'file_name': hander_dic['file_name'],
                        'total_size': file_size
                    }
                    # 发送报头
                    common.set_hander_dic(conn, hander_dic)
                    # 发送真实数据
                    common.send_date(conn, file_path)
                else:
                    print('file path error!!!')
        except ConnectionResetError:
            break
    conn.close()
server.close()




