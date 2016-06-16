#/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class Watcher(FileSystemEventHandler):

    def __init__(self, filename, matcher):
        self.filename = os.path.abspath(filename)
        self.matcher = matcher
        self.observer = Observer()
        self.fd = None
        self.offset = 0
        if os.path.isfile(self.filename):
            self.fd = open(self.filename)
            self.offset = os.path.getsize(self.filename)

    def start(self):
        self.observer.schedule(self, path.dirname(self.filename), recursive=False)
        self.observer.start()
        self.observer.join()

    def stop(self):
        self.observer.stop()
        if self.fd is not None and not self.fd.closed:
            self.fd.close()

    def on_modified(self, event):
        if os.path.abspath(event.src_path) == self.filename:
            self.fd.seek(self.offset, 0)
            match = getattr(self.matcher, 'match', lambda x: False)  #利用反射对传入的matcher做判断是否有match方法，如果没有的话，永远返回False
            for line in self.fd:
                line = line.rstrip('\n')
                if match(line):
                    print("matched {0}".format(line))
            self.offset = self.fd.tell()

    def on_deleted(self, event):
        if os.path.abspath(event.src_path) == self.filename:
            self.fs.close()

    def on_created(self, event):
        if os.path.abspath(event.src_path) == self.filename and os.path.isfile(self.filename)
            self.fd = open(self.filename)
            self.offset = os.path.getsize(self.filename)

    def on_moved(self, event): #分两种情况，一种是从本地移走
        if os.path.abspath(event.src_path) == self.filename: #证明是被移走的，所以直接关掉文件句柄就可以了
            self.fd.close()
        elif os.path.abspath(event.dest_path) == self.filename and os.path.isfile(self.filename):
            self.fd = open(self.filename)
            self.offset = os.path.getsize(self.filename)

if __name__ == '__main__':
    class Matcher:
        def match(self, line):
            return True
    w = Watcher(sys.argv[1], Matcher())
    try:
        w.start()
    except KeyboardInterrupt
        w.stop()
    finally:
        print(1)

