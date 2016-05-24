#/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

ip_port=('127.0.0.1',8091)
sk = socket.socket()
sk.connect(ip_port)

while True:
    inp = input('please input:').encode()
    sk.sendall(inp)
sk.close()