from socket import *
from days31.上传下载 import client_common
from days31.上传下载 import common

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))

USER_MARK=None

def register():
    while True:
        print('please input your register name and password,quit enter q:')
        name=input('name:').strip()
        if name=='q':
            break
        password=input('password:').strip()
        password2=input('confirm password:').strip()
        if name and  password and password2:
            if password2==password:
                res ,msg=client_common.register(client,name,password)
                print(msg)
                if res:
                    break
            else:
                print('the two password are different!!!')
        else:
            print('input error!!!')


def login():
    global USER_MARK
    while True:
        print('please input your name and password,quit enter q:')
        name = input('name:').strip()
        if name == 'q':
            break
        password = input('password:').strip()
        if name and password :
            res, user_mark,msg = client_common.login(client, name, password)
            print(msg)
            if res:
                USER_MARK=user_mark
                break
        else:
            print('input error!!!')

def upload():
    res=common.check_login(client)
    if not res:
        print('please login first')
        return
    while True:
        print('please input upload file path,quit enter q:')
        path = input('file path:').strip()
        if path == 'q':
            break
        if path :
            res, msg = client_common.upload(client, path, USER_MARK)
            print(msg)
            if res:
                break
        else:
            print('input error!!!')

def download():
    res = common.check_login(client)
    if not res:
        print('please login first')
        return
    while True:
        print('please input upload file name and nation path,quit enter q:')
        name = input('file name:').strip()
        if name == 'q':
            break
        path=input('nation path').strip()
        if name and path :
            res, msg = client_common.download(client, USER_MARK,name,path )
            print(msg)
            if res:
                break
        else:
            print('input error!!!')

func_dir={
    '1':register,
    '2':login,
    '3':upload,
    '4':download
}
if __name__ == '__main__':
    while True:
        print('''
        '1':register,
        '2':login,
        '3':upload,
        '4'download                 
        ''')
        choice=input('please choice:').strip()
        if choice not in func_dir:
            print('input error!!!')
        else:
            func_dir[choice]()