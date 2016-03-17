#/usr/bin/env python
# -*- coding: utf-8 -*-

def login(key):
    local = 'wiker'
    if local==key:
        return True
    else:
        return False


def auth(func):
    def inner(*arg,**kwarg):
        key = kwarg.pop("token")
        # key=kwarg["token"]
        # del kwarg["token"]
        is_login=login(key)
        if not is_login:
            return "非法请求"
        func(*arg,**kwarg)
        print("after")
        return func(*arg, **kwarg)
    return inner

@auth
def f4(arg):
    server_list = ['c1','c2','c3']
    return server_list

key="wiker"
print(f4(1,token=key))
# print(f4(1))