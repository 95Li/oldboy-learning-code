import  subprocess
import hashlib
import json
import struct

from socket import *

server=socket(AF_INET,SOCK_STREAM)
server.bind(('192.168.12.108',8083))
server.listen(5)

while True:
    conn, addre = server.accept()
    print(addre)
    while True:
        try:
            msg=conn.recv(1024).decode('utf-8')
            print(msg)
            obj=subprocess.Popen(msg,
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            res_out=obj.stdout.read()
            res_eer=obj.stderr.read()

            m=hashlib.md5()
            m.update(res_out)
            m.update(res_eer)
            #设置报头
            hander_dic={
                'total_size':len(res_out)+len(res_eer),
                'md5':m.hexdigest()
            }
            hander_json=json.dumps(hander_dic)
            hander_bytes=hander_json.encode('utf-8')

            #发送报头的长度
            hander_size=len(hander_bytes)
            conn.send(struct.pack('i',hander_size))

            #发送报头、
            conn.send(hander_bytes)

            #发送真实数据
            conn.send(res_out)
            conn.send(res_eer)
        except ConnectionResetError:
            break
    conn.close()
server.close()




