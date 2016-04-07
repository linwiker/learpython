#/usr/bin/env python
# -*- coding: utf-8 -*-
#hash使用取模，解决冲突方法是拉链法
class Node:
    def __init__(self, key, value):
        self.key = hash(key)
        self.value = value

class Map:
    def __init__(self, init_size):
        self.__slot = [[]] * init_size
        self.__size = init_size

    def put(self, key, value):
        node = Node(key, value)
        address = node.key % self.__size
        self.__slot.append(node)

    def get(self, key, default=None):
        _key = hash(key)
        address = _key % self.__size
        for i in self.__slot[address]:
            if i.key == _key
                return i.value
        return default