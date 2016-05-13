#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Process
from multiprocessing import Manager
import time

li = []

def foo(i):
    li.append(i)
    print('say hi',li)

for i in range(10):
    p = Process(target=foo,args=(i,))
    p.start()

print('ending',li)
