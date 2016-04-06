#/usr/bin/env python
# -*- coding: utf-8 -*-
#用stack实现计算器程式

from stack import Stack

func_map = {  #下面实现的加减乘除功能我们可以通过定义此字典来简单实现
    '+': lambda x, y:x + y,
    '-': lambda x, y:x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

def cacl(expr):  #定义计算函数
    stack = Stack()  #实例化Stack
    for c in expr:
        if c in "(+-*/":   #如果传入的c是"(+-*/"中的一个，则压栈
            stack.push(c)
        else:  #其他情况只有是数字或者")"符号
            if c != ')': #如果不是')'则表示是数字，我们首先传入的都是整数，所以先对数字进行整形处理
                c = int(c)
                if stack.top.value in '+-*/':  #现在看栈的头部，如果栈头部是'+-*/'中的一个，则从栈中压出来
                    s = stack.pop()
                    if isinstance(stack.top.value, int):  #然后现在的栈头部判断是否是整形，如果不是得话，则表示这是个错误的表达式
                        raise Exception('wrong expr')
                    v = stack.pop()  #如果是则把数字压出来
                    v = func_map[s](v,c)  #可以简单通过此方式来实现下面的功能
