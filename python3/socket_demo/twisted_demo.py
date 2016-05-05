#/usr/bin/env python
# -*- coding: utf-8 -*-
event_list = []
def run():
     for event in event_list:
         obj = event()
         obj.execute()

class BaseHandle(object):
    def execute(self):
        raise Exception('you must overwrite execute')

