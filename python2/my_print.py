#!/usr/bin/env python
# -*- coding: utf-8 -*-
#函数被当做参数传入另一个函数
def my_print(name):
    print 'hello %s' % name
def my_print2(name):
    print 'hhhhh %s' % name
def progress(func,name):
    func(name)
progress(my_print,'wd')
progress(my_print2,'pc')
