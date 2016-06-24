#/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import shelve

class Counter:

    def __init__(self, db_path):
        #使用shelve实现数据持久化
        self.db_path = db_path
        self.db = shelve.open(self.db_path, 'c')
        self.lock = threading.Lock()
        self.stoped = False

    def inc(self, name):
        #对规则的名称（name）进行计数
        with self.lock:
            self.db[name] = self.db.get(name, 0) + 1


    def get(self, name):
        #获取规则的数量，如果没有的话则报0
        with self.lock:
            self.db.get(name, 0)

    def clean(self, name):
        #清除规则的计数
        with self.lock:
            self.db.pop(name)

    def stop(self):
        with self.lock:
            if not self.stoped:
                self.db.close()