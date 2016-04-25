#/usr/bin/env python
# -*- coding: utf-8 -*-

def w1(fun):
    def inner():
        print("w1装饰之前")
        fun()
        print("w1装饰之后")
    return inner

def w2(fun):
    def inner():
        print("w2装饰之前")
        fun()
        print("w2装饰之后")
    return inner

@w2
@w1
def f1():
    print("f1")

print(f1.__name__)