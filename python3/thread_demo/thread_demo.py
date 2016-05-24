#/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread

class MyServer(Thread):

    def run(self):
        print("重写Thread的run方法")
        Thread.run(self)

def show(num):
    print(num)

t = MyServer(target=show,args=(100,))
t.start()



