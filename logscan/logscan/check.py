#/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import threading
import datetime
from .notification import Message


class Checker:
    def __init__(self, name, interval, threshold, contacts, counter, notifier):
        #使用config.json传入的值
        self.name = name
        self.interval = interval
        self.threshold = threshold
        self.contacts = contacts
        self.counter = counter
        self.__event = threading.Event()
        self.notifier = notifier

    def __do_check(self):
        #判断是否到达阈值，触发规则则调用报警
        while not self.__event.is_set():
            self.__event.wait(self.interval * 60) #使用wait代替time.sleep的原因是如果我们想退出的话，但是线程还处在sleep
            # 范围内，那么这个进程是没法立刻退出的，wait没有这个问题，退出的话直接就可以退出了，不需要再次等待
            count = self.counter.get(self.name)
            self.counter.clean(self.name)
            if count >= self.threshold[0]:
                if count < self.threshold[1] or self.threshold[1] < 0:
                    self.notify(count)

    def start(self):
        threading.Thread(target=self.__do_check, name="checker-{0}".format(self.name)).start()

    def notify(self, count):
        for contact in self.contacts:
            message = Message(contact, self.name, count, datetime.datetime.now())
            self.notifier.notify(message)

    def stop(self):
        self.__event.set()

