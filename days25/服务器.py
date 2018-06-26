import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind(('192.168.12.152',8088))
phone.listen(5)

while True:
    # phone.accept()
    conn,client_addr=phone.accept()
    print(client_addr)
    print('建立连接')
    while True:
        msg=conn.recv(1024)
        print(msg.decode('utf-8'))
        re=input('responce')
        conn.send(re.encode('utf-8'))

    conn.close()

phone.close()
