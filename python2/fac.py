#!/usr/bin/env python
# -*- coding: utf-8 -*-
#计算阶乘，比如5!=5*4*3*2*1
#第一种解法
total = 0
def fac(num):
    n = 1
    for i in range(1,num+1):
        n = n * i
    print n
fac(10)
fac(1)

#第二种解法
def fac(num):
    if num > 1:
        return num*fac(num-1)
    else:
        return 1
print fac(10)
print fac(1)
print fac(100)
