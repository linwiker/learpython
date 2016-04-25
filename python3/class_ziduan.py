#/usr/bin/env python
# -*- coding: utf-8 -*-

class Province:
    country = '中国'  #静态字段
    def __init__(self, name):
        self.name = name #普通字段

#直接访问普通字段
obj = Province('河北省')
print(obj.name)

#直接访问静态字段
print(Province.country)