#/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import threading

def send_mail(user, message):
    pass

class Checker:

    def __init__(self, name, expr, path, interval, threshold, users, counter):
        #使用config.json传入的值
        self.name = name
        self.expr = expr
        self.path = path
        self.interval = interval
        self.threshold = threshold
        self.users = users
        self.counter = counter
        self.__event = threading.Event()

    def check(self):
        #判断是否到达阈值，触发规则则调用报警
        while not self.__event.is_set():
            self.__event.wait(self.interval * 60) #使用wait代替time.sleep的原因是如果我们想退出的话，但是线程还处在sleep
            # 范围内，那么这个进程是没法立刻退出的，wait没有这个问题，退出的话直接就可以退出了，不需要再次等待
            count = self.counter.get(self.name)
            self.counter.clean(self.name)
            if count >= self.threshold[0]:
                if count < self.threshold[1] or self.threshold < 0:
                    self.notify('{0} matched {1} times in {2}min'.format(self.name, count, self.interval))

    def notify(self, message):
        for user in self.users:
            t = threading.Thread(target=send_mail, args=(user, message), name='mail_send-{0}'.format(user))
            t.start()
            t.join()

    def stop(self):
        self.__event.set()

