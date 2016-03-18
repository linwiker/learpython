#/usr/bin/env python
# -*- coding: utf-8 -*-

# def func(arg1,arg2):
#     if arg1==0:
#         print(arg1,arg2)
#     arg3=arg1+arg2
#     if arg3 > 1000:
#         return arg3
#     return func(arg2,arg3)
#
# print(func(0,1))
def n5():
    return 1500

def n4():
    return n5()

def n3():
    return n4()

def n2():
    return n3()

def n1():
    return n2()

f =n1
print(n1.__name__)