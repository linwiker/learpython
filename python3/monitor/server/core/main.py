#/usr/bin/env python
# -*- coding: utf-8 -*-

from .redisHelper import RedisHelper

class MonitorServer():
    def __init__(self):
        self.r = RedisHelper()
        self.r.set('k1','v1')
        self.r.get('k1')

    def start(self):
        pass
