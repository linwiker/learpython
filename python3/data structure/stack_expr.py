#/usr/bin/env python
# -*- coding: utf-8 -*-
#用stack实现计算器程式

from stack import Stack


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
                    if s == '+':  #如果s压出来的是'+'号，则对压出来的数字和c进行相加，下面其他都以此类推
                        v = v + c
                    if s == '-':
                        v = v - c
                    if s == '*':
                        v = v * c
                    if s == '/':
                        v = v / c