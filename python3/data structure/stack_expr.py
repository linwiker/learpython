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
        elif c.strip() == '':
            pass
        else:  #其他情况只有是数字或者")"符号
            if c != ')': #如果不是')'则表示是数字，我们首先传入的都是整数，所以先对数字进行整形处理
                c = int(c)
                if stack.top.value in '+-*/':  #现在看栈的头部，如果栈头部是'+-*/'中的一个，则从栈中压出来
                    s = stack.pop()
                    if not isinstance(stack.top.value, (int,float)):  #然后现在的栈头部判断是否是整形，如果不是得话，则表示这是个错误的表达式
                        raise Exception('wrong expr')
                    v = stack.pop()  #如果是则把数字压出来
                    v = func_map[s](v,c)  #可以简单通过此方式来实现下面的功能
                    stack.push(v)  #把计算的v进行压栈
                else:  #如果不是上面的符号之一，则直接压栈
                    stack.push(c)
            else:   #这是c==‘）’情况
                if isinstance(stack.top.value, (int,float)): #如果栈的头部是整数或者浮点型，则弹出此值
                    v = stack.pop()
                    if stack.top.value == '(': #如果栈的头部值是（则弹出丢掉，然后把v的值压到栈里面
                        stack.pop()
                        stack.push(v)
                    else:  #其他情况则表示是错误的
                        raise Exception('wrong expr')
                else:
                     raise Exception('wrong expr')
    while stack.top:  #判断栈的头部是不是空值，如果不是则把数值压出来
        j = stack.pop()
        if not isinstance(j, (int,float)):  #判断是不是整形或者浮点型数字，如果不是则抛出错误
            raise Exception('wrong expr')
        if stack.top.value in '+-*/':  #如果栈的头部是'+-*/'，则把此值压出来
            s = stack.pop()
            if not isinstance(stack.top.value, (int, float)): #然后再进行判断此是否是整形或者浮点型，如果不是则报错
                raise Exception('wrong expr')
            v = stack.pop()  #其他情况则压出此值，然后进行加减乘除运算
            v = func_map[s](v,j)
            if stack.top is None:  #如果栈头部值是空，则返回v
                return v
        else:  #其他情况抛出错误
            raise Exception('wrong shuzi')

if __name__ == '__main__':
    print(cacl('(3+4)*5/((2+3)*3)'))


