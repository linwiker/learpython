#/usr/bin/env python
# -*- coding: utf-8 -*-

from .redisHelper import RedisHelper
from .serialize import push_all_configs_into_redis
from conf import hosts
import json
import time
import threading


class MonitorServer():
    def __init__(self):
        self.r = RedisHelper()
        self.save_configs()

    def start(self):
        self.data_handle()
        self.handle()

    def save_configs(self):
        push_all_configs_into_redis(self, hosts.monitored_groups)

    def handle(self):
        chan_sub = self.r.subscribe()
        while True:
            service_data=chan_sub.parse_response()
            service_data = json.loads(service_data[2].decode())
            service_data['timestap'] = time.time()
            service_data_key = ("ServerData::%s::%s" %(service_data['host'],service_data['service']))
            self.r.set(service_data_key,json.dumps(service_data['data']))

    def data_handle_run(self):
        data_process(self)

    def data_handle(self):
        """处理监控数据，独立线程"""
        t = threading.Thread(target=self.data_handle_run)
        t.start()

    def alter_handle(self):
        """处理报警信息，独立线程"""
        pass






















