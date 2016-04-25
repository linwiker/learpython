#/usr/bin/env python
# -*- coding: utf-8 -*-
# class Goods(object):
#
#     @property
#     def price(self):
#         print('@property')
#
#     @price.setter
#     def price(self, value):
#         print('@price.setter')
#         print(value)
#
#     @price.deleter
#     def price(self):
#         print('@price.deleter')
#
# #调用
# obj = Goods()
# obj.price  #自动执行@property修饰的price方法，并获取方法的返回值
# obj.price = 123 #自动执行@price.setter修饰的price方法，并将123赋值给对方的参数
# del obj.price #自动执行@price.deleter修饰的price方法
# #输出结果
class Goods(object):
    def __init__(self):
        #原价
        self.original_price = 100
        #折扣
        self.discount = 0.8

    @property
    def price(self):
        #实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value
        print(value)
    @price.deleter
    def price(self):
        del self.original_price

obj = Goods()
print(obj.price)
obj.price = 200

del obj.price