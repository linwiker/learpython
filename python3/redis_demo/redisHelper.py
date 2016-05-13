#/usr/bin/env python
# -*- coding: utf-8 -*-
import redis

class RedisHelper:
    pool = redis.ConnectionPool(host='10.99.56.124',port=6379,max_connections=1024)
    def __init__(self):
        self.__conn = redis.Redis(connection_pool=pool)
        self.chan_sub = 'fm90'
        self.chan_pub = 'fm80'

    def publish(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub



