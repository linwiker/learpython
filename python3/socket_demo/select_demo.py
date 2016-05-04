# !/usr/bin/env python
# -*- coding: utf-8 -*-
#获取屏幕输入字段

import select
import threading
import sys

while True:
    readable, writeable, error = select.select([sys.stdin,],[],[],1)
    if sys.stdin in readable:
        print('select get stdin:',sys.stdin.readline())
