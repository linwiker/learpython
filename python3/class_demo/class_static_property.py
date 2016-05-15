#/usr/bin/env python
# -*- coding: utf-8 -*-
# class Foo:
#     def get_bar(self):
#         return "wiker"
#
#     BAR = property(get_bar)
#
# obj = Foo()
# result = obj.BAR #自动调用get_bar方法，并获取方法的返回值
# print(result)
class Foo:
    def get_bar(self):
        return "wiker"
    #必须两个参数
    def set_bar(self, value):
        return 'set value' + value
        print(value)

    def del_bar(self):
        return 'zhou'
    BAR = property(get_bar, set_bar, del_bar, 'description...')

obj = Foo()
obj.BAR  #自动调用第一个参数中定义的方法：get_bar
obj.BAR = 'alex' #自动调用第二个参数中定义的方法：set_bar方法，并将“alex”当做参数传入
obj.BAR.__doc__ ##自动调用第四个参数中定义的方法：description...
del Foo.BAR  #自动调用第三个参数中定义的方法：del_bar方法


