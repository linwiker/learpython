#/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing

def writer_proc(q):
    q.put(1, block = False)

def reader_proc(q):
    print(q.get(block = False))

if __name__ == '__main__':
    q = multiprocessing.Queue()
    writer = multiprocessing.Process(target=writer_proc, args=(q,))
    writer.start()
    reader = multiprocessing.Process(target=reader_proc, args=(q,))
    reader.start()

    writer.join()
    reader.join()