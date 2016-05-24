#/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time

gl_num = 0
samp = threading.BoundedSemaphore(4)

def show(arg):
    samp.acquire()
    global gl_num


    time.sleep(1)
    gl_num +=1
    print(gl_num)
    samp.release()


for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()

print('main thread stop')