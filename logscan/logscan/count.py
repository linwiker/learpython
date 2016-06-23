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
        with self.lock:
            self.db[name] = self.db.get(name, 0) + 1


    def get(self, name):
        with self.lock:
            self.db.get[name, 0]

    def clean(self, name):
        with self.lock:
            self.db.pop(name)

    def stop(self):
        with self.lock:
            if not self.stoped:
                self.db.close()


if __name__ == '__main__':
    import logging
    import time
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line: %(lineno)d] %(levelname)s %(message)s [%(threadName)s]',
                    datefmt='%a, %d %b %Y %H:%M:%S')
    counter = Counter()

    def inc(counter):
        for x in range(10):
            counter.inc()
            time.sleep(0.2)
    def get(counter):
        time.sleep(0.2)
        logging.debug("Current value is {0}".format(counter.val))

    inc1 = threading.Thread(target=inc, name='inc1', args=(counter,))
    inc2 = threading.Thread(target=inc, name='inc2', args=(counter,))
    g = threading.Thread(target=get, name='get', args=(counter,))

    inc1.start()
    inc2.start()
    g.start()