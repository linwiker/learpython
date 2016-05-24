#/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing
import time

def proc1(pipe):
    while True:
        for i in range(10000):
            print("send:%s" %(i))
            pipe.send(i)
            time.sleep(1)

def proc2(pipe):
    while True:
        print("proc2 rec:", pipe.recv())
        time.sleep(1)

def proc3(pipe):
    while True:
        print("proc3 rev:" ,pipe.recv())
        time.sleep(1)

if __name__ == '__main__':
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc1, args=(pipe[0],))
    p2 = multiprocessing.Process(target=proc2, args=(pipe[1],))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
