#/usr/bin/env python
# -*- coding: utf-8 -*-
class Node:  #定义结点类
    def __init__(self,data):
        self.data = data   #数据
        self.next = None  #定义指针


class LinkedList:
    def __init__(self):
        self.head = None  #定义链表头
        self.tail = None  #定义链表尾

    def append(self,data): #追加操作
        node = Node(data)
        if self.head is None: #如果头为空，即代表是新链表，所以这个时候头和尾都是node
            self.head = node
            self.tail = node
        else:                 #否则是尾的指针指向新加入的node，并且node就是新的尾部
            self.tail.next = node
            self.tail = node

    def iter(self): #定义遍历操作
        if self.head is None: #如果头直接为空，则直接return None
            return None
        cur = self.head  #定义头部等于头部，就相当于做了一个游标指向头部
        yield cur.data  #然后直接返回头部的值
        while cur.next: #然后判断当前指针的下一条是否为空，如果不为空则把游标指向下一条，并返回其值
            cur = cur.next
            yield cur.data

