#!/usr/bin/env python
# -*- coding: utf-8 -*-
import memcache

client_list = [('127.0.0.1:11211',1),('127.0.0.1:11212',1),('127.0.0.1:11213',1)]

mc = memcache.Client(client_list,debug = True)
for i in range(100):
    mc.set(str(i),'test')
