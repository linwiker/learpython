#/usr/bin/env python
# -*- coding: utf-8 -*-
#二叉树遍历方法
from stack import Stack
from queue import Queue

class Node:
    def __init__(self, value):  #定义树节点，树的节点有左右两个
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, node):
        self.node = node

    def add_left(self, tree):  #添加左加点
        self.node.left = tree

    def add_right(self, tree): #添加右节点
        self.node.right = tree

    @property  #定义左右两个属性，在遍历的时候使用
    def left(self):
        return self.node.left

    @property
    def right(self):
        return self.node.right

    def visit_first(self, fn):  #定义先序遍历
        fn(self.node.value)  #先遍历我们的根节点，然后从树的左节点进行遍历，然后在右节点
        if self.left:
            self.left.visit_first(fn)
        if self.right:
            self.right.visit_first(fn)

    def visit_midd(self, fn):  #定义中序遍历
        if self.left:   #先遍历树的左节点，然后遍历树的根节点，然后再遍历树的右节点
            self.left.visit_midd(fn)
        fn(self.node.value)
        if self.right:
            self.right.visit_midd(fn)

    def visit_after(self, fn): #定义后序遍历
        if self.left:  #先遍历树的左节点，然后遍历树的右节点，然后再遍历树的根节点
            self.left.visit_after(fn)
        if self.right:
            self.right.visit_after(fn)
        fn(self.node.value)

    def visit_first_nocur(self, fn):  #使用非递归的方式实现先序遍历，要使用栈来实现
        stack = Stack()  #首先初始化一个栈
        stack.push(self)  #然后把整个树都压到栈里面
        while stack.top:  #只要是栈里面有数据就执行此循环
            p = stack.pop()  #把栈里面的第一个节点压出来
            fn(p.node.value)  #然后使用fn函数执行根节点
            if p.right:  #树是从左边开始执行，所以我们先把右边树节点压到栈里面(因为栈是先进后出)
                stack.push(p.right)
            if p.left:  #然后把左节点压到栈里面
                stack.push(p.left)

    def visit_level(self, fn):   #实现层次遍历,要使用队列来实现
        queue = Queue()  #初始化队列
        queue.put(self)  #把书放进队列里面
        while not queue.empty():  #只要队列不为空，就一直循环
            q = queue.get()  #压出队列的头部的节点
            fn(q.node.value)  #使用fn执行树的根节点
            if q.left:  #从左边开始把树的节点压到队列中，队列是先进先出，所以从树左边开始进队列
                queue.put(q.left)  #把树的左节点压到队列中
            if q.right:   #如果树有右节点，也把树的右节点压到队列中
                queue.put(q.right)


if __name__ == '__main__':
    d = Tree(Node('D'))  #定义树的所有节点
    e = Tree(Node('E'))
    b = Tree(Node('B'))
    b.add_left(d)
    b.add_right(e)
    f = Tree(Node('F'))
    g = Tree(Node('G'))
    c = Tree(Node('C'))
    c.add_left(f)
    c.add_right(g)
    a = Tree(Node('A'))
    a.add_left(b)
    a.add_right(c)

    from functools import partial
    a.visit_first(partial(print, end=''))  #打印先序遍历
    print('\r')
    a.visit_midd(partial(print, end=''))   #打印中序遍历
    print('\r')
    a.visit_after(partial(print, end=''))  #打印后序遍历
    print('\r')
    a.visit_first_nocur(partial(print, end=''))  #使用栈的方式打印出先序遍历，尽量少使用递归，结果和使用递归的打印先序遍历结果一样
    print('\r')
    a.visit_level(partial(print, end=''))  #打印出层次遍历的而结果，结果是ABCDEFG
