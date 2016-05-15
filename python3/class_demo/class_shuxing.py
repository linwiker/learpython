#/usr/bin/env python
# -*- coding: utf-8 -*-
class Foo:
    def func(self):
        return "方法"
    #定义属性
    @property
    def prop(self):
        return "属性"

#调用
foo_obj = Foo()

print(foo_obj.func())
print(foo_obj.prop) #调用属性