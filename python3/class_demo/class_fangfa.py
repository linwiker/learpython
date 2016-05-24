#/usr/bin/env python
# -*- coding: utf-8 -*-
class Foo:
    __val = 4
    def __init__(self, name):
        self.name = name

    def ord_func(self):
        print('普通方法')
        return self.__val

    @classmethod
    def class_func(cls):
        print('类方法')
        return cls.__val

    @staticmethod
    def static_func():
        print('静态方法')
        return val


#调用类方法
# Foo.__class_func
# print(Foo.val)
# print(Foo.class_func())
a = Foo('wiker')
print(a.class_func())

