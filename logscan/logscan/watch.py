#/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import threading
from queue import Queue
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from .match import MatcherChain

class Watcher(FileSystemEventHandler):

    def __init__(self, filename, counter):
        self.filename = os.path.abspath(filename)
        self.queue =  Queue()
        self.matcherchain = MatcherChain(queue=self.queue, counter)
        self.observer = Observer()
        self.fd = None
        self.offset = 0

        if os.path.isfile(self.filename):
            self.fd = open(self.filename)
            self.offset = os.path.getsize(self.filename)

    def start(self):
        self.matchers.start()
        self.observer.schedule(self, os.path.dirname(self.filename), recursive=False)
        self.observer.start()
        self.observer.join()

    def stop(self):
        self.matcherchain.stop()
        self.observer.stop()
        if self.fd is not None and not self.fd.closed:
            self.fd.close()

    def on_modified(self, event):
        if os.path.abspath(event.src_path) == self.filename:
            self.fd.seek(self.offset, 0)
            for line in self.fd:
                line = line.rstrip('\n')
                self.queue.put(line)
            self.offset = self.fd.tell()

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

if __name__ == '__main__':
    class Matcher:
        def match(self, line):
            return True
    w = Watcher(sys.argv[1], Matcher())
    w2 = Watcher(sys.argv[2], Matcher())
    try:
        t1 = threading.Thread(target=w.start)
        t1.start()
        t2  = threading.Thread(target=w2.start)
        t2.start()
    except KeyboardInterrupt:
        t1._stop()
        t2._stop()


