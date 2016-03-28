#/usr/bin/env python
# -*- coding: utf-8 -*-

# #创建类
# class Foo:
#     def Bar(self):
#         print('Bar')
#     def Hello(self, name):
#         print('I am %s' % name)
# #根据Foo创建对象obj
# obj = Foo()
# obj.Bar()
# obj.Hello('wiker')

class Foo:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def detail(self):
        print(self.name)
        print(self.age)
# obj1 = Foo('wiker', 19)
# print(obj1.name)
# print(obj1.age)
obj2 = Foo('zhou', 18)
obj2.detail()