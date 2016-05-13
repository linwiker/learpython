#/usr/bin/env python
# -*- coding: utf-8 -*-
<<<<<<< HEAD
from multiprocessing import Process,Array

temp = Array('i',[11,22,33,44])

def Foo(i):
    temp[i] = 100+i
    for item in temp:
        print(i,'------->',item)

for i in range(2):
    p = Process(target=Foo,args=(i,))
    p.start()
=======
import multiprocessing

def f(n, a):
    n.value = 3.14
    a[0] = 5

if __name__ == '__main__':
    num = multiprocessing.Value('d',0.0)
    arr = multiprocessing.Array('i',range(10))
    p = multiprocessing.Process(target=f, args=(num, arr))
    p.start()
    p.join()
    print(num.value)
    print(arr[:])
>>>>>>> cf5b9792d3e8061920f1171134637f8fbbab4068
