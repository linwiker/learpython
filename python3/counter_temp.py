#/usr/bin/env python
# -*- coding: utf-8 -*-
# import collections
# data=collections.Counter("sadahsidhsidhsidhishdisahdiisahd")
# print(data)
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs


f1,f2,f3=count()
print(f1())
print(f2())
print(f3())