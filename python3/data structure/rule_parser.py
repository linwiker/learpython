#/usr/bin/env python
# -*- coding: utf-8 -*-
from stack import Stack

def match(exprs, line, fn):
    stack = Stack()
    is_expr = False
    expr = []  #暂存器
    for c in exprs:
        if c == '#':  #c等于#情况
            if not is_expr:
                is_expr = True
            else:
                is_expr = False
                v = fn(line, ''.join(expr))  #把需要匹配的值赋值给v，这个v是一个布尔值
                expr = []  #清空暂存器
                if stack.top is None:  #stack栈里面还有个(号，所以这个判断语句不会执行
                    stack.push(v)
                    continue
                s = stack.pop()  #执行此语句，再从栈里面取出里面的元素，第一次的时候取出来的应该是(，所以都不满足下面的条件，直接执行最下面的压栈语句，把s和v都压进栈里面
                if s == '!':
                    v = not v
                    if stack.top is None:
                        stack.push(v)
                        continue
                    s = stack.pop()
                if s == '&':
                    if isinstance(stack.top.value, bool):
                        v = stack.pop() and v
                        stack.push(v)
                    else:
                        raise Exception('wrong expr')
                elif s == '|':
                    if isinstance(stack.top.value, bool):
                        v = stack.pop() or v
                        stack.push(v)
                    else:
                        raise Exception('wrong expr')
                elif s == '(':
                    stack.push(s)
                    stack.push(v)
                else:
                    raise Exception('wrong expr')
        else:
            if is_expr:
                expr.append(c)
            else:
                if c in '(&!|':
                    stack.push(c)
                elif c.strip() == '':
                    pass
                elif c == ')':
                    v = stack.pop()
                    if not isinstance(v, bool):
                        raise Exception('wrong expr')
                    s = stack.pop()
                    if s == '!':
                        v = not v
                        s = stack.pop()
                    if s == '(':
                        stack.push(v)
                    else:
                        raise Exception('wrong expr')
                else:
                    raise Exception('wrong expr')
    while stack.top:
        v = stack.pop()
        if not isinstance(v, bool):
            raise Exception('wrong expr')
        s = stack.pop()
        if s == '!':
            v = not v
            s = stack.pop()
        if s == '&':
            v2 = stack.pop()
            if not isinstance(v2, bool):
                raise Exception('wrong expr')
            v = v and v2
        elif s == '|':
            v2 = stack.pop()
            if not isinstance(v2, bool):
                raise Exception('wrong expr')
            v = v or v2
        else:
            raise Exception('wrong expr')
        if stack.top is None:
            return v
        else:
            stack.push(v)

if __name__ == '__main__':
    import re
    line = 'abc 123 def 456 asd 789'
    exprs = '(#abc# & #324#) | (!#def# & #789#)'

    def callback(line, expr):
        return re.match(expr, line) is not None

    print(match(exprs, line, callback))