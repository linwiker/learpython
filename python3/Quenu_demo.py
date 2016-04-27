#/usr/bin/env python
# -*- coding: utf-8 -*-
import queue
q = queue.Queue(maxsize=10)
for i in range(15):
    q.put(i)
    if q.full():
        print(q.get())