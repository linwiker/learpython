#!/usr/bin/env python
# -*- coding: utf-8 -*-
def name(name=3,world=4):
    print '%s,%s' % (name,world)
name(world=1,name=2)
name(1)
name(world=5)
name()

def hello(*params):
    print params
hello(1,2,3,4,56,7,8)
