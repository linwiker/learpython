#/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

ip_port=('127.0.0.1',8090)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)

while True:
    data = sk.recv(1024)
    print('receive:',data.decode())
    inp = input('please input:').encode()
    sk.sendall(inp)
    if inp == 'exit':
        break

sk.close()