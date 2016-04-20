#/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import threading
import select

def Process(request, client_address):
    print(request, client_address)
    conn = request
    conn.sendall('欢迎致电，请拨打分机号'.encode())
    flag = True
    while flag:
        data = conn.recv(1024).decode()
        if data == 'exit':
            flag = False
        elif data == '0':
            conn.sendall('您的通话可能会被录音.........'.encode())
        else:
            conn.sendall('请重新输入。'.encode())

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(('127.0.0.1',8093))
sk.listen(5)

while True:
    r, w, e = select.select([sk,],[],[],1)
    print('looping')
    if sk in r:
        print('get request')
        request,client_address = sk.accept()
        t = threading.Thread(target=Process, args=(request, client_address))
        t.daemon = False
        t.start()

sk.close()