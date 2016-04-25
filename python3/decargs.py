#/usr/bin/env python
# -*- coding: utf-8 -*-

def Before(request,kargs):
    print("%s %s http://before//index" % (request,kargs))

def After(request,kargs):
    print("%s %s http://after//index" % (request,kargs))

def Access(before_func,after_func):
    def outer(main_func):
        def wrapper(request,kargs):

            before_result = before_func(request,kargs)
            if before_result != None:
                return before_result

            main_result = main_func(request,kargs)
            if main_result != None:
                return main_result

            after_result = after_func(request,kargs)
            if after_result != None:
                return after_result

        return wrapper
    return outer

@Access(Before,After)
def Index(request,kargs):
    print("%s %s http://index//" %(request,kargs))

Index("get","-A")

print(Index.__name__)