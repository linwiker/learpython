#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kazoo.client import KazooClient
import time
zk = KazooClient(hosts='10.99.56.111:2181,10.99.56.112:2181,10.99.56.113:2181')
zk.start()

@zk.DataWatch('/tmp')
def changed(data, stat, event):
    print("-----DataWatch-----")
    print("data:", data)
    print("stat:", stat)
    print("event:", event)

zk.create('/tmp', b'value1')
time.sleep(2)
zk.set('/tmp', b'value2')
time.sleep(2)
zk.delete('/tmp')
time.sleep(2)
