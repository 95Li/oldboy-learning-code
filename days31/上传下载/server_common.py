
import os,json,time
import struct,hashlib
from ..上传下载 import common

BASE_PATH='F:\python\object\days2\days31\上传下载\服务器fv\\user'

def login(conn, hand_info):
    path=os.path.join(BASE_PATH,hand_info['user_name'])
    if os.path.exists(path):
        with open(path,'r',encoding='utf-8')as f:
            user_info=json.load(f)
        if user_info['user_password']==hand_info['user_password']:
            now_time=time.time()
            msg=str(now_time)+hand_info['user_name']
            mark= common.my_md5(msg)
        else:
            mark=None
    else:
        mark=None

    result_dic = {
        'operation_type': '1',
        'mark': mark
    }
    common.send_hander_dic(conn, result_dic)
    return mark


def register(conn, hand_info):
    path = os.path.join(BASE_PATH, hand_info['user_name'])
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8')as f:
            hand_info.pop('operation_type')
            json.dump(hand_info,f)
            res=True
    else:
        res=False
    result_dic = {
        'operation_type': '1',
        'res': res
    }
    common.send_hander_dic(conn, result_dic)

def upload(conn, hand_info,mark):
    acc_mark=hand_info['mark']
    if acc_mark==mark:
        conn.send(True.encode('utf-8'))
        total_size = hand_info['total_size']

        # 根据size获取文件内容
        file_path = os.path.join(BASE_PATH, '%s.txt' % hand_info['file_name'])
        common.get_date_by_size(conn, file_path, total_size)
    else:
        conn.send(False.encode('utf-8'))


def download(conn, hand_info,mark):
    acc_mark = hand_info['mark']
    if acc_mark == mark:
        conn.send(True.encode('utf-8'))
        file_path = os.path.join(BASE_PATH, '%s.json' % hand_info['file_name'])

        file_size = os.path.getsize(file_path)
        # 设置报头
        hander_dic = {
            'operation_type': '2',
            'file_name': hand_info['file_name'],
            'total_size': file_size
        }
        # 发送报头
        common.set_hander_dic(conn, hander_dic)
        # 发送真实数据
        common.send_date(conn, file_path)

    else:
        conn.send(False.encode('utf-8'))
