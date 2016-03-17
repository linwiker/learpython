#/usr/bin/env python
# -*- coding: utf-8 -*-
def inject_user(default_user):
    def inject(fn):
        def wrap(*args,**kwargs):
            if 'user' not in kwargs.keys():
                kwargs['user'] =default_user
            return fn(*args,**kwargs)
            return wrap.__closure__
        return wrap
    return inject

@inject_user('comyn')
def do_something(*args,**kwargs):
    print(kwargs['user'])

print(do_something.__closure__)