#/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request

def Geturl(url):
    with request.urlopen(url) as f:
        data = f.read()
        print('Status:',f.status,f.reason)
        for k,v in f.getheaders():
            print('%s:%s' % (k,v))
        print('Data:',data.decode('utf-8 '))

#Geturl('https://api.douban.com/v2/book/2129650')
