#/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing

def f(x, arr, l):
    x.value = 3.14
    arr[0] = 5
    l.append('hello')

if __name__ == '__main__':
    server = multiprocessing.Manager()
    x = server.Value('d',0.0)
    arr = server.Array('i', range(10))
    l = server.list()

    proc = multiprocessing.Process(target=f, args=(x,arr,l))
    proc.start()
    proc.join()

    print(x.value)
    print(arr)
    print(l)