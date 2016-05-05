#/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing

def writer_proc(q):
    try:
        q.put(1, block = False)
    except:
        pass

def reader_proc(q):
    try:
        print(q.get(block = False))
    except:
        pass

if __name__ == '__main__':
    q = multiprocessing.Queue()
    writer1 = multiprocessing.Process(target=writer_proc, args=(q,))
    writer1.start()
    writer2 = multiprocessing.Process(target=writer_proc, args=(q,))
    writer2.start()
    writer3 = multiprocessing.Process(target=writer_proc, args=(q,))
    writer3.start()
    reader = multiprocessing.Process(target=reader_proc, args=(q,))
    reader.start()

    writer1.join()
    writer2.join()
    writer3.join()
    reader.join()
