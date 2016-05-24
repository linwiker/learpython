#/usr/bin/env python
# -*- coding: utf-8 -*-

class BaseService():
    def __init__(self):
        self.name = 'BaseService'
        self.interval = 300
        self.plugin_name = 'your_plugin_name'
        self.triggers = {}
