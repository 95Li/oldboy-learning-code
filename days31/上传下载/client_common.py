'''
        '1':register,
        '2':login,
        '3':upload,
        '4'download
'''
import json
import struct
import os
from ..上传下载 import common



def register(client,name,password):
    password = common.my_md5(password)
    # 设置报头
    hander_dic = {
        'operation_type': '1',
        'user_name':name,
        'user_password':password
    }
    common.send_hander_dic(client, hander_dic)
    res_dic=common.accept_hander(client)
    if res_dic['res']:
        return True,'register successful'
    else:
        return False,'register user alearty exists!!!'



def login(client, name, password):
    password=common.my_md5(password)
    # 设置报头
    hander_dic = {
        'operation_type': '2',
        'user_name': name,
        'user_password': password
    }
    common.send_hander_dic(client, hander_dic)
    res_dic =common.accept_hander(client)
    if res_dic['mark']:
        return True,res_dic['mark'],'login successful'
    else:
        return False,None,'user name or password error!!!'


def  upload(client, path, mark):
    if os.path.exists(path):
        file_size = os.path.getsize(path)

        file_name=path.spilt('\\')[-1]
        print(file_name)
        # 设置报头
        hander_dic = {
            'operation_type': '3',
            'file_name':file_name,
            'mark': mark,
            'total_size': file_size
        }
        # 发送报头
        common.send_hander_dic(client, hander_dic)
        check = common.accept_hander(client).decode('utf-8')
        if check:
            # 发送真实数据
            common.send_date(client, path)
            return True,'upload successful'
        else:
            return True,'账户异常,请重新登录！！！'
    else:
        return False,'file path error!!!'




def download(client, mark,name,path ):
    # 设置报头
    hander_dic = {
        'operation_type': '4',
        'file_path': None,
        'file_name':name,
        'mark': mark
    }
    # 发送报头
    common.send_hander_dic(client, hander_dic)
    check=common.accept_hander(client).decode('utf-8')
    if check:
        res_dic =common.accept_hander(client)
        total_size=res_dic['total_size']

        #根据size获取文件内容
        file_path = os.path.join(path, name)
        common.get_date_by_size(client, file_path, total_size)
        return True,'download successful'
    else:
        return True,'账户异常,请重新登录！！！'
