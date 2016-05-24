#!/usr/bin/env python
# -*- coding: utf-8 -*-
from redisHelper import RedisHelper

obj = RedisHelper()
for i in range(1000000):
    obj.publish('{0} Hello World!'.format(i))
