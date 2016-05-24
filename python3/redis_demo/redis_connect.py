#/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

pool = redis.ConnectionPool(host='10.99.56.124',port=6379,max_connections=1024)
r = redis.Redis(connection_pool=pool)

pipe = r.pipeline(transaction=False)

r.set('fo1','Bar')
r.set('role1','wiker')
pipe.execute()


print(r.get('fo1'))
print(r.get('role1'))