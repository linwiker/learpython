#!/usr/bin/env python
# -*- coding: utf-8 -*-
#猜字游戏
from random import randint

x = randint(0,300)
for count in range(50):
    digit = input('please input a number:')
    if digit == x:
        print "Bingo"
        break
    elif digit > x:
        print 'Too large,please try again:'
    else:
        print 'Too small,try again'
