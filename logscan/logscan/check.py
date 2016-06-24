#/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import logging
import threading
from queue import Queue, Full


class Message:
    def __init__(self, user, name, path, count, type = None):
        self.user = user
        self.name = name
        self.path = path
        self.count = count
        if type == None:
            self.type = ['mail',] #如果一条消息要使用多个方式发送的话，可以使用此方式实现

class Notification:
    def __init__(self):
        self.message = None
        self.__event = threading.Event()
        self.__cond = threading.Condition()
        self.__mail_queue = Queue(100)

    def _send_mail(e, q):
        #从mail队列里面取消息进行发送（此方法是实际发送mail的线程）
        while not self.__event.is_set():
            message = self.__mail_queue.get()
            #TODO

    def send_mail(self):
        #等待notify方法来通知然后把消息put进mail的队列里面
        threading.Thread(target=self._send_mail, name='send-mail-real').start()
        while not self.__event.is_set():
            with self.__cond:
                self.__cond.wait()
                if 'mail' in self.message.type:
                    try:
                        self.__mail_queue.put(self.message, timeout=1)
                    except Full:
                        logging.error('mail queue is full')


    def send_sms(self):
        while not self.__event.is_set():
            with self.__cond:
                self.__cond.wait()
                #TODO

    def notify(self, message):
        #使用self__cond来生产消息，然后消息生产完以后通知指定的方式进行消息的发送
        with self.__cond:
            self.message = message
            self.__cond.notify_all()

    def start(self):
        mail = threading.Thread(target=self.send_mail, args=(self.__event) name='send_mail')
        mail.start()
        sms = threading.Thread(target=send_sms, name='send_sms')
        sms.start()




class Checker:

    def __init__(self, name, expr, path, interval, threshold, users, counter, notification):
        #使用config.json传入的值
        self.name = name
        self.expr = expr
        self.path = path
        self.interval = interval
        self.threshold = threshold
        self.users = users
        self.counter = counter
        self.__event = threading.Event()
        self.notification = notification

    def start(self):
        #判断是否到达阈值，触发规则则调用报警
        while not self.__event.is_set():
            self.__event.wait(self.interval * 60) #使用wait代替time.sleep的原因是如果我们想退出的话，但是线程还处在sleep
            # 范围内，那么这个进程是没法立刻退出的，wait没有这个问题，退出的话直接就可以退出了，不需要再次等待
            count = self.counter.get(self.name)
            self.counter.clean(self.name)
            if count >= self.threshold[0]:
                if count < self.threshold[1] or self.threshold < 0:
                    self.notify('{0} matched {1} times in {2}min'.format(self.name, count, self.interval))

    def notify(self, count):
        for user in self.users:
            message = Message(user, self.name, self.path, count)

    def stop(self):
        self.__event.set()

