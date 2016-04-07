#/usr/bin/env python
# -*- coding: utf-8 -*-
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:   #定义栈，两个方法push和pop
    def __init__(self):
        self.top = None

    def push(self, value):  #入栈
        node = Node(value)
        node.next = self.top  #结点的下一条既是栈顶，因为我们是压入的node，所以现在的栈顶既是node
        self.top = node

    def pop(self):  #出栈
        node = self.top  #定义node为栈顶，我们压出去一个节点就表面栈顶变为了node指针指向的下一条，然后返回node值
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