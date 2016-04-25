#/usr/bin/env python
# -*- coding: utf-8 -*-
#第一种方法
# def check(allow):
#     def deco(fn):
#         def wrap(username,*args,**kwargs):
#             if username in allows:
#                 return fn(username,*args,**kwargs)
#             return "not allow"
#         wrap.__name__ = fn.__name__
#         wrap.__doc__ = fn.__doc__
#         return wrap
#     return deco
#
# @check(['wiker','zhou'])
# def process(*args,**kwargs):
#     ''' this is test help file'''
#     pass
#
# print(process.__name__)
# print(process.__doc__)
from functools import wraps
def check(allows):
    def deco(fn):
        @wraps(fn)
        def wrap(username,*args,**kwargs):
            if username in allows:
                return fn(username,*args,**kwargs)
            return "not allow"
        return wrap
    return deco

@check(['wiker','zhou'])
def process(username):
    ''' this is test help file'''
    print("认证成功")
# #测试输出
# print(process.__name__)
# print(process.__doc__)
process('wiker')


