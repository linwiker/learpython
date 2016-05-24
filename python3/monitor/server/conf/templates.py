#/usr/bin/env python
# -*- coding: utf-8 -*-
from .services import linux

class BaseTemplate():
    def __init__(self):
        self.name = 'your template name'
        self.host = []
        self.services = []

class LinuxGenericTemplate(BaseTemplate):
    def __init__(self):
        super(LinuxGenericTemplate, self).__init__()
        self.name = 'LinuxCommonServices'
        self.services = [
            linux.CPU(),
            linux.Memory()
        ]

class Linux2(BaseTemplate):
    def __init__(self):
        super(Linux2, self).__init__()
        self.name = 'linux2'
        self.services = [
            linux.CPU(),
            linux.NetWork()
        ]

