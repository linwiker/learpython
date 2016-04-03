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
    for i in range(10):
        stack.push(i)

    while stack.top:  #会看到反过来把我们插入的数值输出
        print(stack.pop())