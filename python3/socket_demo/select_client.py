#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

messages = [ 'This is the message.',
             'It will be sent',
             'in parts.'
           ]

server_address = ('localhost',10000)

socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM),
         socket.socket(socket.AF_INET, socket.SOCK_STREAM),
        ]

print('connecting to %s port %s'%(server_address))
for s in socks:
    s.connect(server_address)

for message in messages:
    for s in socks:
        print('%s:sending %s' %(s.getsockname(),message))
        s.send(message.encode())
    for s in socks:
        data = s.recv(1024).decode()
        print('%s: received %s' %(s.getsockname(), data.decode()))
        if not data:
            print('closing socket',s.getsockname())
