#/usr/bin/env python
# -*- coding: utf-8 -*-

# class F1:
#     pass
#
# class S1(F1):
#     def show(self):
#         print('S1.show')
#
# class S2(F1):
#     def show(self):
#         print('S2.show')
#
# def Func(obj):
#     print(obj.show())
#
#
# s1_obj=S1()
# Func(s1_obj)
#
# s2_obj=S2()
# Func(s2_obj)

_metaclass_ =type #确定使用新式类
class calculator:

    def count(self,args):
        return 1

calc = calculator() #自定义类型

from random import choice
obj=choice(['hello,world',[1,2,3],calc]) #obj是随机返回的，类型不确定
print(obj.count('a')) #方法多态