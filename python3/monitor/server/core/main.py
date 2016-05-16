#/usr/bin/env python
# -*- coding: utf-8 -*-

from .redisHelper import RedisHelper
from .serialize import push_all_configs_into_redis
from conf import hosts


class MonitorServer():
    def __init__(self):
        self.r = RedisHelper()
        self.save_configs()

    def start(self):
        pass

    def save_configs(self):
        push_all_configs_into_redis(self, hosts.monitored_groups)