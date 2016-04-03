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

    def insert(self, idx, value):  #定义插入操作
        cur = self.head  #初始化cur和cur的id
        cur_idx = 0
        if cur is None:  #添加判断是否为空链表
            node = Node(value)
            self.head = node
            self.tail = node
        elif cur.next is None:
            if idx == 0:  #判断链表插入头部
                node = Node(value)   #待解决
                self.head = node
                cur.next = node.next
                node.next = cur
            else:
                node =Node(value)
                node.next = cur.next
                cur.next = node
        else:
            if idx == 0:
                node = Node(value)
                self.head = node
                node.next = cur
                cur.next = node.next.next
            else:
                while cur_idx < idx - 1: #排除idx-1序列之前，以及超过定义超过索引值的抛出错误
                    cur = cur.next
                    if cur is None:
                        raise Exception("list length less than index")
                    cur_idx += 1
                node = Node(value)    #实例化Node
                node.next = cur.next  #实例化Node的下一跳游标等于当前值cur（这个地方的值是idx-1位置的值）的下一跳游标的值，简单点意思就是把原来idx位置的值向后移动
                cur.next = node    #idx的值赋值成node的值
                if node.next is None:  #判断node的值要插入到最后位置，把尾部标识要移动到node上
                    self.tail = node
        #print(self.head.data)

    def remove(self, idx): #添加删除索引位置方法
        cur = self.head
        cur_idx = 0
        if cur is None:  #判断链表是否为空
            raise Exception("list length less than index")
        elif cur.next is None: #链表只有一个元素的情况
            if idx != 0:
                raise Exception("list length less than index")
        else:
            if idx == 0:
                self.head = cur.next
            else:
                while cur_idx < idx - 1:
                    cur = cur.next
                    if cur is None:
                        raise Exception("list length less than index")
                    cur_idx += 1
                cur.next = cur.next.next  #直接把cur的下一跳指针指向他的下下一跳
                if cur.next is None:
                    self.tail = cur
        #print(self.tail.data)

    def len(self):    #计算长度方法
        cur = self.head
        cur_idx = 0
        if cur is None:  #判断链表是否为空
            return 0
        else:
            while True:
                cur = cur.next
                cur_idx += 1
                if cur is None:
                    return cur_idx
                    break

if  __name__ == '__main__':
    link_list = LinkedList()
    for i in range(10):
        link_list.append(i)
    link_list.insert(3,100)
    link_list.remove(5)
    print(link_list.len())
    for y in link_list.iter():
        print(y)