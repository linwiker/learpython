#/usr/bin/env python
# -*- coding: utf-8 -*-
#平衡二叉树
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
        fn(self.node.value)
        if self.left:
            self.left.visit_first(fn)
        if self.right:
            self.right.visit_first(fn)

    def visit_midd(self, fn):  #定义中序遍历
        if self.left:
            self.left.visit_midd(fn)
        fn(self.node.value)
        if self.right:
            self.right.visit_midd(fn)

    def visit_after(self, fn): #定义后序遍历
        if self.left:
            self.left.visit_after(fn)
        if self.right:
            self.right.visit_after(fn)
        fn(self.node.value)


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
