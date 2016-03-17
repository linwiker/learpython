#/usr/bin/env python
# -*- coding: utf-8 -*-

# class Foo:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def kanchai(self):
#         print("%s, %d岁, %s,上山砍柴" %(self.name, self.age, self.gender))
#
# xiaoming = Foo('小明',10,'男')
# xiaoming.kanchai()

class Person:

    def __init__(self, na, gen, age, fig):
        self.name = na
        self.gender = gen
        self.age = age
        self.fight = fig

    def grassland(self):
        self.fight = self.fight - 200

cang = Person('苍井空','女',18,1000)
print(cang.grassland())
print(cang.fight)