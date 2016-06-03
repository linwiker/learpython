#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, LoggingEventHandler
# from watchdog.observers.api import ObservedWatch

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == "/tmp/watch.log":
            print("log file %s changed" % event.src_path)

if __name__ == '__main__':
    event_handler1 = MyHandler()
    observer = Observer()
    watch = observer.schedule(event_handler1, path="/" ,recursive=True)


    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler2 = LoggingEventHandler()
    observer.add_handler_for_watch(event_handler2, watch)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()