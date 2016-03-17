#/usr/bin/env python
# -*- coding: utf-8 -*-
class ClassProerty:
    def __init__(self,fn):
        self.fn = fn
    def __get__(self,instance,cls):
        return self.fn(cls)

class Spam:
    __val = 3
    @ClassProerty
    def val(cls):
        return cls.__val

    @ClassProerty
    def name(cls):
        return cls.__name__.lower()

s = Spam()
print(s.val)

print(s.name)