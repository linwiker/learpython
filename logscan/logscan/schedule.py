#/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from os import path
from base64 import urlsafe_b64decode
from watchdog.observers import Observer
from .watch import Watcher
from .count import Counter
from .notification import Notifier
from .persistence import OffsetPersistence

class Schedule:
    def __init__(self, config):
        self.observer = Observer()
        self.handlers = {}
        self.watchers = {}
        self.counter = Counter()
        self.notifier = Notifier(config)
        self.offset_db = OffsetPersistence(config)

    def __make_key(self, filename):
        return path.abspath(urlsafe_b64decode(filename).decode())

    def add_watcher(self, filename):
        #如果监控的文件都在同一个目录下，下面这种方法只会启动一个inotify来进行监控这个目录下的所有文件，handler.start实际上调用了monitor的start
        filename = self.__make_key(filename)
        if handler.filename not in self.handlers.keys():
            handler = Watcher(filename, counter=self.counter, notifier=self.notifier, offset_db=self.offset_db)
            if path.dirname(handler.filename) not in self.watchers.keys():
                self.watchers[path.dirname(handler.filename)] = self.observer.schedule(handler, path.dirname(handler.filename), recursive=False)
            else:
                watch = self.watchers[path.dirname(handler.filename)]
                self.observer.add_handler_for_watch(handler, watch)
            self.handlers[handler.filename] = handler
            handler.start()


    def remove_watcher(self, filename):
        #判断key是否在watchers里面，有则从observer中剔除，然后从watchers字典内删除，并把handlers剔除并stop
        key = self.__make_key(filename)
        handler = self.handlers.pop(key)
        if handler is not None:
            watch = self.watchers[path.dirname(key)]
            self.observer.remove_handler_for_watch(handler, watch)
            handler.stop()
            if not self.observer._handlers[watch]:
                self.observer.unschedule(watch)
                self.watchers.pop(path.dirname(handler.filename))


    #添加和移除monitor，实质上就是调用Monitor类的add和remove方法来操作
    def add_monitor(self, filename, name, src):
        key = self.__make_key(filename)
        handler = self.handlers.get(key)
        if handler is None:
            logging.warning('watcher {0} not found, auto add it'.format(filename))
            handler.add_watcher(filename)
            handler = self.handlers.get(key)
        handler.monitor.add(filename, name, src)

    def remove_monitor(self, filename, name):
        key = self.__make_key(filename)
        handler = self.handlers.get(key)
        if handler is None:
            logging.warning('watcher {0} not found'.format(filename))
            return
        handler.monitor.remove(name)

    def start(self):
        self.observer.start()
        self.notifier.start()

    def join(self):
        self.observer.join()

    def stop(self):
        self.observer.stop()
        for handler in self.handlers.values():
            handler.stop()
        self.notifier.stop()
        self.offset_db.close()

