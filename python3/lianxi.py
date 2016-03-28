#/usr/bin/env python
# -*- coding: utf-8 -*-
# class Foo:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     def get(self):
#         print(self.__name)
#         print(self.__age)
#     def __set(self,i):
#         self.__age += i
#
# obj=Foo('wiker',20)
# obj.get()
# obj.__set(20)
# obj.get()
# class Goods(object):
#
#     def __init__(self):
#         # 原价
#         self.original_price = 100
#         # 折扣
#         self.discount = 0.8
#
#     def get_price(self):
#         # 实际价格 = 原价 * 折扣
#         new_price = self.original_price * self.discount
#         return new_price
#
#     def set_price(self, value):
#         self.original_price = value
#
#     def del_price(self):
#         del self.original_price
#
#     PRICE = property(get_price, set_price, del_price, '价格属性描述...')
#
# obj = Goods()
# print(obj.PRICE)      # 获取商品价格
# obj.PRICE = 200 # 修改商品原价
# print(obj.PRICE)
# print(obj.PRICE.__doc__)
# del obj.PRICE     # 删除商品原价
# class C:
#     __name = "公有静态字段"
#
#     def func(self):
#         print(C.__name)
#
# class D(C):
#
#     def show(self):
#         print(C.__name)
#
#
# # print(C.__name)    #不可以访问会报错
#
# # obj = C()
# # obj.func()      #类内部可以访问
#
# obj_son = D()
# obj_son.show()    #派生类中可以访问
# class C:
#
#     def __init__(self):
#         self.__foo = "公有字段"
#
#     def func(self):
#         print(self.__foo)
#
# class D(C):
#
#     def show(self):
#         print(self.__foo)
#
# obj = C()
#
# # # print(obj.__foo)     # 通过对象访问
# # # obj.func()  # 类内部访问
# # # #
# # obj_son = D();
# # obj_son.show()  # 派生类中访问
# print(obj._C__foo)
class Foo(object):
    def __getslice__(self,i,j):
        print('__getslice__',i,j)
    def __setslice__(self, i, j, sequence):
        print('__setslice__',i,j)
    def __delslice__(self, i, j):
        print('__delslice__', i, j)

obj = Foo()

obj[0:1]