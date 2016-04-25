#/usr/bin/env python
# -*- coding: utf-8 -*-
#源码级别解析property装饰器
class Property:
    def __init__(self,fget=None,fset=None,fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, cls):
        if self.fget is not None:
            return self.fget(instance)
    def __set__(self, instance, value):
        if self.fset is not None:
            self.fset(instance,value)
    def __delete__(self, instance):
        if self.fdel is not None:
            self.fdel(instance)
    def getter(self,fn):
        self.fget = fn
    def setter(self,fn):
        self.fset = fn
    def deler(self,fn):
        self.fdel = fn

class Spam:
    def __init__(self,val):
        self.__val =val
    @Property
    def val(self):
        return self.__val
    @val.setter
    def set_val(self,value):
        self.__val = value

s = Spam(3)
print(s.val)  #s.val等同于Spam.val.__get__(s,Spam)
s.val = 5
print(s.val) #等同于Spam.val.__set__(s,value)