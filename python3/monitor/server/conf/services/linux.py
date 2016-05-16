#/usr/bin/env python
# -*- coding: utf-8 -*-
from .generic import BaseService

class CPU(BaseService):
    def __init__(self):
        super(CPU, self).__init__()
        self.interval = 30
        self.name = 'linux_cpu'
        self.plugin_name = 'get_cpu_status'
        self.triggers = {
            'idle':{
                'func':'avg',
                'last': 10*60,
                'count': 1,
                'operator': 'lt',
                'warning': 20,
                'critical': 5,
                'data_type': float
            },
            'iowait': {
                'func':'hit',
                'last': 15*60,
                'count': 5,
                'operator': 'gt',
                'warning': 20 ,
                'critical': 50,
                'data_type': float
            }
        }


class Memory(BaseService):
    def __init__(self):
        super(Memory, self).__init__()
        self.name = 'linux_mem'
        self.interval = 20
        self.plugin_name = 'get_mem_status'
        self.triggers = {
            'usage': {
                'func':'avg',
                'last': 5*60,
                'count': 1,
                'operator': 'gt',
                'warning': 80,
                'critical': 90,
                'data_type': float

            }
        }

class NetWork(BaseService):
    def __init__(self):
        super(NetWork, self).__init__()
        self.interval = 60
        self.name = 'linux_network'
        self.plugin_name = 'get_network_status'
