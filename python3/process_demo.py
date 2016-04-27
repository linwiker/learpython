#/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing

def f(name):
    print('hello {0}'.format(name))
for i in range(10):
    p = multiprocessing.Process(target=f, args=('world',))
    p.start()