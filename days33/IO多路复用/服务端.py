from socket import *
import select

s=socket()
s.bind(('127.0.0.1',8080))
s.listen(5)
s.setblocking(False)

r_list=[s,]
w_list=[]
w_date={}
while True:
    r1,wl,x1=select.select(r_list,w_list,[],0.5)
    """
     rlist -- wait until ready for reading
    wlist -- wait until ready for writing
    xlist -- wait for an ``exceptional condition''
    If only one kind of condition is required, pass [] for the other lists.    
    """
    for r in r1:
        if r1==s:
            conn,addre=s.accept()
            r_list.append(conn)
        else:
            try:
                date=r.recv(1024)
                if not date:
                    r.close()
                    r_list.remove(r)
                    continue
                w_list.append(r)
                w_date[r]=date.upper()
            except ConnectionResetError :
                r.close()
                r_list.remove(r)
                continue

    for w in wl:
       w.send(w_date[w])
       w_list.remove(w)
       w_date.pop(w)






