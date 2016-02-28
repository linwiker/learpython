#!/usr/bin/env python
# -*- coding: utf-8 -*-
read_me = '''Function annotation syntax has been a Python feature since version 3.0 (PEP 3107), however the semantics of annotations has been left undefined.
Experience has shown that the majority of function annotation uses were to provide type hints to function parameters and return values. It became evident that it wo    uld be beneficial for Python users, if the standard library included the base definitions and tools for type annotations.
PEP 484 introduces a provisional module to provide these standard definitions and tools, along with some conventions for situations where annotations are not availa    ble.
For example, here is a simple function whose argument and return type are declared in the annotations:'''
#统计并且按照循序排序
l = list(read_me)
z = {i:l.count(i) for i in l}
l1=z.items()
for j in range(len(l1)-1):
    for i in range(len(l1)-1-j):
        if l1[i][1] > l1[i+1][1]:
            l1[i],l1[i+1] = l1[i+1],l1[i]
l1.reverse()
for k in range(10):
    print l1[k][0],l1[k][1]


print('-')*100

#第二种解法
d2 = {}
for s in list(read_me):
    d2[s] = d2.get(s,0)+1
print d2
