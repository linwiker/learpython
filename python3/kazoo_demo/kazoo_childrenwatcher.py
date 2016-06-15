#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kazoo.client import KazooClient
import time

zk = KazooClient(hosts="10.99.56.111:2181,10.99.56.112:2181,10.99.56.113:2181")
zk.start()

@zk.ChildrenWatch("/tmp")
def childWatch(children):
    print("----------------ChildWatch--------------")
    print("children:", children)

zk.create("/tmp/a", b"value1")
time.sleep(2)
zk.set("/tmp/a", b"value2")
time.sleep(2)
zk.delete("/tmp/a")
time.sleep(2)

