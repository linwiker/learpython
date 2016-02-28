#!/usr/bin/env python
# -*- coding: utf-8 -*-
#演示递归的实现方式,以斐波拉契数列作为演示
#就是后一个值是前面两值的和

#普通的实现方式
def fib(n):
    a,b = 0,1
    count = 1
    while count < n:
        a,b = b,a+b
        count = count +1
    print b
fib(20)

#递归的实现方式
def fib(n):
    if n == 0 or n ==1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
print fib(20)
