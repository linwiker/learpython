#/usr/bin/env python
# -*- coding: utf-8 -*-
from .redisHelper import RedisHelper
from conf import settings
import json
import time
from plugins import plugin_api
import threading

class MonitorClient():
    def __init__(self):
        self.r = RedisHelper()
        self.ip = settings.ClientIP
        self.host_config = self.get_host_config()

    def start(self):   #开启监控
        self.handle()

    def get_host_config(self):  #取服务器端配置信息
        config_key = ("HostConfig::%s" %self.ip)
        config = self.r.get(config_key)
        if config:
            config = json.loads(config.decode())
        print(config)
        return config


    def handle(self):  #根据配置信息进行监控
        if self.host_config:
            while True:
                for service,val in self.host_config.items():
                    if len(val) < 3:
                        self.host_config[service].append(0)
                    plugin_name,interval,last_run_time = val
                    service_time = time.time() - last_run_time
                    if service_time < interval:
                        next_run_time = interval - service_time
                        print("server %s next run time in %s " %(service,next_run_time))
                    else:
                        #print("run %s" %service)
                        self.host_config[service][2] = time.time()
                        t = threading.Thread(target=self.call_plugin, args=(service, plugin_name))
                        t.start()
                time.sleep(10)
        else:
            raise Exception("无法获取到主机配置信息")

    def call_plugin(self, service_name, plugin_name):
        func = getattr(plugin_api, plugin_name)
        service_data = func()
        report_data = {
            'host': self.ip,
            'service': service_name,
            'data': service_data
        }
        self.r.publish(json.dumps(report_data))