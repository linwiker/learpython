#/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
from conf import settings

class RedisHelper:
    def __init__(self):
        pool = redis.ConnectionPool(host=settings.RedisServer,port=settings.RedisPort,max_connections=settings.RedisMaxconn)
        self.__conn = redis.Redis(connection_pool=pool)
        self.chan_sub = settings.RedisSubChannel
        self.chan_pub = settings.RedisPubChannel

    def publish(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub



