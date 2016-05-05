#/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

ip_port=('0.0.0.0',8090)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    conn,address = sk.accept()
    conn.sendall('欢迎致电，请输入分机号码。'.encode())
    flag = True
    while flag:
        data = conn.recv(1024).decode()
        if data == 'exit':
            flag = False
        elif data == '0':
            conn.sendall('通话可能会被录音，...........'.encode())
        else:
            conn.sendall('请重新输入'.encode())
    conn.close()


