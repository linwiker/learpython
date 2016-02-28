#!/usr/bin/env python
# -*- coding: utf-8 -*-
#把传入的所有数字参数进行相加，饼输入结果
def addall(username,*parame):
 #   temp_list=list(parame)
    n=0
    for i in parame:
        n=n+i
    print '%s has %s yuan' % (username,n)
addall('wd',1,2,3,4.1)
addall(44,1,2,3,4.1)

def print_params(*name,**params):
    print name
    print params
print_params(name='pc',job='worker',location='bj')
