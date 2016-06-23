#/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
from os import path
from .count import Counter

class Schedule:

    def __init__(self, counter_path):
        self.watchers = {}
        self.threads = {}
        self.counter = Counter(counter_path)

    def add_watcher(self, watcher):
        #判断watcher线程是否启动，如果没启动的话，启动个watcher线程
        if watcher.filename not in self.watchers.keys():
            watcher.counter = self.counter
            t = threading.Thread(target=watcher.start, name="Watcher-{0}".format(watcher.filename))
            t.setDaemon(True)
            t.start()
            self.threads[watcher.filename] = t
            self.watchers[watcher.filename] = watcher

    def remove_watcher(self, filename):
        #移除watcher，如果key在watchers的字典里，则进行删除
        key = path.abspath(filename)
        if key in self.watchers.keys():
            self.watchers[key].stop()
            self.watchers.pop(key)
            self.threads.pop(key)
    
    def join(self):
        #当watchers字典内有值的话，首先利用list拷贝一份，然后对其再进行循环。
        while self.watchers.values():
            for t in list(self.threads.values()):
                t.join()

    def stop(self):
        for w in self.watchers.values():
            w.stop()
        self.counter.stop()

