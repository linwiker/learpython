#/usr/bin/env python
# -*- coding: utf-8 -*-
#队列python实现方式
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, value):  #入队，首先判断是否为空队列，如果是空队列，则首尾都等于插入的节点（我们此处都想象队列无限大）
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:  #非空队列的话，在尾部插入节点，然后把尾部指向新插入的节点
            self.tail.next = node
            self.tail = node

    def pop(self):  #出队，首先判断是否是空队列，空队列直接报错，非空队列删除头部节点并返回其值
        if self.head is None:
            raise Exception('empty queue')
        else:
            node = self.head
            self.head = node.next
            return node.value

if __name__ == '__main__':
    q = Queue()
    for i in range(10):
        q.put(i)
    for _ in range(10):
        print(q.pop())