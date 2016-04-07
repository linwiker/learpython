#/usr/bin/env python
# -*- coding: utf-8 -*-
#hash使用取模，解决冲突方法是拉链法
class Node:
    def __init__(self, key, value): #定义插入hash的节点，key要经过hash计算，所以key要是可以进行hash的值
        self.key = hash(key)
        self.value = value

class Map:
    def __init__(self, init_size):  #初始化hash表，hash槽初始化（使用list进行存储），个数取决于我们给的初始化的个数，定义最大的hash个数
        self.__slot = [[]] * init_size
        self.__size = init_size

    def put(self, key, value): #定义put方法
        node = Node(key, value)
        address = node.key % self.__size  #位置使用
        self.__slot[address].append(node)

    def get(self, key, default=None):
        _key = hash(key)
        address = _key % self.__size
        for i in self.__slot[address]:
            if i.key == _key
                return i.value
        return default