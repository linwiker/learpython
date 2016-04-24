#/usr/bin/env python
# -*- coding: utf-8 -*-

import socketserver
import os

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        base_path = 'D:/test'
        conn = self.request
        print("connected........")
        while True:
            pre_data = conn.recv(1024)
            cmd,filename,file_size = pre_data.split('|')
            recv_size = 0
            file_dir = os.path.join(base_path,filename)
            with open(file_dir,'wb') as f:
                Flag = True
                while Flag:
                    if int(filename) > recv_size:
                        data = conn.recv(1024)
                        recv_size += len(data)
                    else:
                        recv_size = 0
                        Flag = False
                        continue

                    f.write(data)
                print("upload successed")

instance = socketserver.ThreadingTCPServer(('127.0.0.1',8194),MyServer)
instance.serve_forever()
