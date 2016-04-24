#/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import os
import sys

ip_port = ('127.0.0.1',8194)
sk = socket.socket()
sk.bind(ip_port)

container = {'key':'','data':''}
while True:
    input = input('path:')
    cmd,path = input.split("|")
    file_name = os.path.basename(path)
    file_size = os.stat(path).st_size
    sk.send(cmd+"|"+file_name+"|"+str(file_size))
    send_size = 0
    with open(path,'rb') as f:
        Flag = True
        while Flag:
            if send_size + 1024 > file_size:
                data = f.read(file_size - send_size)
                Flag = False
            else:
                data = f.read(1024)
                send_size += 1024
            sk.send(data)

sk.close()