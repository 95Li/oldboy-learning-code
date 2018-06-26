from socket import *
import time

s=socket()
s.bind(('172.0.0.1',8080))
s.listen(5)
s.setblocking(False)

r_list=[]
w_list=[]

while True:
    try:
        conn,addr=s.accept()
        r_list.append(conn)
    except BlockingIOError:
        print('ganhuo')
        print('rlist',len(r_list))

        del_rlist=[]
        for conn in r_list:
            try:
                date=conn.recv(1024)
                w_list.append((conn,date.upper()))
            except BlockingIOError :
                continue
            except ConnectionResetError:
                del_rlist.append(conn)

        del_wlist=[]
        for item in w_list:
            try :
                conn=item[0]
                date=item[1]
                conn.send(date)
                del_wlist.append(item)
            except BlockingIOError :
                continue
            except ConnectionResetError:
                del_wlist.append(item)

        for conn in del_rlist:
            r_list.remove(conn)
        for item in del_wlist:
            w_list.remove(item)


