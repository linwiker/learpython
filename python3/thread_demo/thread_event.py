#/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time
def do(arg):
    print('start')
    arg.wait()
    print('execute')

event = threading.Event()
for i in range(2):
    t = threading.Thread(target=do, args=(event,))
    t.start()

print(event.isSet())
event.set()
print(event.isSet())

