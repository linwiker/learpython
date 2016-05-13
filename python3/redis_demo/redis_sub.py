#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
r = redis.Redis()
sub = r.pubsub()
sub.subscribe('fm80')
sub.parse_response()
while True:
    z=sub.parse_response()
    print(z)
