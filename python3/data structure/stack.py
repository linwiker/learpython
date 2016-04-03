#/usr/bin/env python
# -*- coding: utf-8 -*-
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:   #定义栈，两个方法push和pop
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        node = self.top
        self.top = node.next
        return node.value

if __name__ == '__main__':
    stack = Stack()
#栈实现括号匹配
    exp = '{a * [x/(x+y)]}'
    for c in exp:
        if c in '{[(': #如果是{[(则进行压栈
            stack.push(c)
        elif c in '}])': #如果是}])则与栈顶的数值进行比较
            v = stack.top.value  #栈顶值
            if c == '}' and v !=  '{':
                raise Exception('{faild}')
            if c == ']' and v !=  '[':
                raise Exception('[faild]')
            if c == ')' and v !=  '(':
                raise Exception('(faild)')
            stack.pop()
    if stack.top is None:  #如果栈抛空了则输出OK，没有抛空输出异常
        print('OK')
    else:
        raise Exception('faild')