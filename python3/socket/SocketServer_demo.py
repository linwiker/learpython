#/usr/bin/env python
# -*- coding: utf-8 -*-
import socketserver

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        conn = self.request
        conn.sendall('欢迎致电，请拨打分机号。'.encode())
        flag = True
        while flag:
            data = conn.recv(1024).decode()
            if data == 'exit':
                flag = False
            elif data == '0':
                conn.sendall('通话可能会被录音。。。。。。。。。。。。。。。。'.encode())
            else:
                conn.sendall('请重新输入'.encode())

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8092),MyServer)
    server.serve_forever()
