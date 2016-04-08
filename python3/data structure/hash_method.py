#/usr/bin/env python
# -*- coding: utf-8 -*-
#此函数默认使用hash做，我们改为可以使用指定hash方式
class Node:
    def __init__(self, key, value): #定义插入hash的节点
        self.key = key
        self.value = value

class Map:
    def __init__(self, init_size ,hash=hash):  #初始化hash表，hash槽初始化（使用list进行存储），个数取决于我们给的初始化的个数，定义最大的hash个数,可以指定hash函数
        self.__slot = [[]] * init_size
        self.__size = init_size
        self.hash = hash

    def put(self, key, value): #定义put方法
        node = Node(key, value)
        address = self.hash(node.key) % self.__size  #计算插入位置使用取模
        self.__slot[address].append(node)  #插入到上面计算的地址的位置的槽里面

    def get(self, key, default=None):  #取数据，定义默认值，如果在槽里面没有找到这个key，则返回默认值
        _key = self.hash(key)
        address = _key % self.__size
        for i in self.__slot[address]:
            if i.key == _key:
                return i.value
        return default

    def remove(self, key):
        address = self.hash(key) % self.__size
        for idx, node in enumerate(self.__slot[address].copy()):
            if node.key == key:
                self.__slot[address].pop(idx)

if __name__ == '__main__':
    map = Map(10)
    for i in range(20):
        map.put(i,i)
    map.remove(10)
    for i in range(20):
        print(map.get(i))
