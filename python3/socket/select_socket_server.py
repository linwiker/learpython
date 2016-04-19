#/usr/bin/env python
# -*- coding: utf-8 -*-
#利用select实现伪同时处理多个socket客户端请求，服务端实现

import select
import socket

sk1 = socket.socket()
sk1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk1.bind(('127.0.0.1',8091))
sk1.listen(5)
sk1.setblocking(0)

inp = [sk1,]

while True:
    readable_list, writeable_list, error_list = select.select(inp, [], inp, 1)
    for r in readable_list:
        if sk1 == r:
            print('accept')
            request, address = r.accept()
            request.setblocking(0)
            inp.append(request)
            print(inp)
        else:
            received = r.recv(1024)
            if received:
                print('received data:',received)
            else:
                inp.remove(r)
sk1.close()
