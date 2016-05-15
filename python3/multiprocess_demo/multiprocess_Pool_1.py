#/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing
import time

def func(msg):
    print("msg:",msg)
    time.sleep(3)
    print("end")

if __name__ == '__main__':
    pool = multiprocessing.Pool(3)
    for i in range(7):
        msg = "hello %d" %(i)
        pool.apply_async(func, (msg,)) #维持秩序的进程总数为3个，当一个进程执行完毕后，会添加到新的进程进去。

    print("Mark~ Mark~ Mark................")
    pool.close() #调用join之前，先调用close函数，否则会报错。执行完close后不会有新的进程加入到pool，join函数等待所有子进程结束。
    pool.join()
    print("Sub-process(es) done.")