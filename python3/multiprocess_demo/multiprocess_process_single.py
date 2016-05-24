#/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process
import time

def worker(interval):
    n = 5
    while n > 0:
        print("The time is {0}".format(time.ctime()))
        time.sleep(interval)
        n -= 1

if __name__ == '__main__':
    p = Process(target=worker, args=(3,))
    p.start()
    print("p.pid:",p.pid)
    print("p.name:",p.name)
    print("p.is_alive:",p.is_alive())


