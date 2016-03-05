#/usr/bin/env python
# -*- coding: utf-8 -*-


def auth(func):
    def inner():
        print("before")
        func()
    return inner

def auth_arg(func):
    def inner(arg):
        print('before')
        func(arg)
        print('after')

def f1():
    print('f1')

def f2(arg):
    print("f2",arg)