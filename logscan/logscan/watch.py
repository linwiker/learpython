#/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
from datetime import datetime
from queue import Queue,Full
from watchdog.events import FileSystemEventHandler
from .monitor import Monitor

class Watcher(FileSystemEventHandler):
    def __init__(self, filename, counter, notifier, offset_db, queue_len=1000):
        self.filename = os.path.abspath(filename)
        self.queue =  Queue(queue_len)
        self.counter = counter
        self.monitor = Monitor(self.queue, counter, notifier)
        self.offset_db = offset_db
        self.timer = datetime.now()
        self.fd = None
        self.offset = 0
        #从持久化存储中读取此文件上次读取的位置和当前获取的位置进行对比，然后进行操作
        if os.path.isfile(self.filename):
            self.fd = open(self.filename)
            offset = self.offset_db.get(self.filename)
            file_size = os.path.getsize(self.filename)
            if offset < 0:
                self.offset = file_size
            else:
                if offset <= file_size:
                    self.offset = offset
                else:
                    self.offset = 0

    def start(self):
        self.monitor.start()

    def stop(self):
        if self.fd is not None and not self.fd.closed:
            self.fd.close()
        self.monitor.stop()
        #持久化文件读到什么位置
        self.offset_db.put(self.filename, self.offset)
        self.offset_db.sync()

    def on_modified(self, event):
        now = datetime.now()
        if os.path.abspath(event.src_path) == self.filename:
            self.fd.seek(self.offset, 0)
            for line in self.fd:
                line = line.rstrip('\n')
                try:
                    self.queue.put_nowait(line)
                except Full:
                    logging.warning("queue overflow")
            self.offset = self.fd.tell()
        if (now - self.timer).seconds > 30:
            self.offset_db.put(self.filename, self.offset)
            self.timer = now

    def on_deleted(self, event):
        if os.path.abspath(event.src_path) == self.filename:
            self.fd.close()

    def on_created(self, event):
        if os.path.abspath(event.src_path) == self.filename and os.path.isfile(self.filename):
            self.fd = open(self.filename)
            self.offset = os.path.getsize(self.filename)

    def on_moved(self, event): #分两种情况，一种是从本地移走，另一种是移到本地
        if os.path.abspath(event.src_path) == self.filename: #证明是被移走的，所以直接关掉文件句柄就可以了
            self.fd.close()
        elif os.path.abspath(event.dest_path) == self.filename and os.path.isfile(self.filename): #移动过来的
            self.fd = open(self.filename)
            self.offset = os.path.getsize(self.filename)

    def __eq__(self, other):
        return self.filename == other.filename

    def __ne__(self, other):
        return self.filename != other.filename

    def __hash__(self):
        return hash(self.filename)

