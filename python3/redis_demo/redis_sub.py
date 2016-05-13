#!/usr/bin/env python
# -*- coding:utf-8 -*-
#import redis
#r = redis.Redis()
#sub = r.pubsub()
#sub.subscribe('fm80')
#sub.parse_response()
#while True:
#    z=sub.parse_response()
#    print(z)
import redisHelper

obj = redisHelper.RedisHelper()
redis_sub = obj.subscribe()
while True:
    msg = redis_sub.parse_response()
    print(msg)

