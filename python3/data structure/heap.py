#/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import random

class Heap:
    def __init__(self):
        self.__data = []

    def insert(self, value):
        self.__data.append(value)
        #计算出索引长度和父节点的索引位置
        idx = len(self.__data) - 1
        parent = math.floor((idx - 1) / 2)
        #有父节点而且父节点的值小于插入的值，执行下面的值和父节点替换操作
        while parent >= 0 and self.__data[parent] < value:
            self.__data[idx] = self.__data[parent]
            self.__data[parent] = value
            idx = parent
            parent = math.floor((idx - 1) / 2)

    def view(self):
        print(self.__data)

    def pop(self):
        if not self.__data:
            raise Exception('list is empty')
        ret = self.__data[0]
        value = self.__data.pop()
        self.__data[0] = value
        idx = 0
        left = 2 * idx + 1
        right = 2 * idx + 2
        while len(self.__data) > left:
            tmp_idx = left
            if len(self.__data) > right and self.__data[right] > self.__data[left]:
                tmp_idx = right
            if self.__data[tmp_idx] > value:
                self.__data[idx] = self.__data[tmp_idx]
                self.__data[tmp_idx] = value
            else:
                return ret
            idx = tmp_idx
            left = 2 * idx + 1
            right = 2 * idx + 2
        return ret

#根据给出的索引，删除二叉树中相应的值
    def remove(self, i):
        if len(self.__data)-1 < i: #如果给出的索引值大于二叉堆中总长度就报错
            raise Exception('超出索引长度')
        ret = self.__data[i]
        value = self.__data.pop()
        self.__data[i] = value
        idx = i
        left = 2 * idx + 1
        right = 2 * idx + 2
        #首先判断总的长度大约左节点索引值，然后把左右节点中比较大的值和二叉堆中最后的值进行比较，如果大于最后的值，则互相交互位置，然后再进行比较
        while len(self.__data) > left:
            tmp_idx = left
            if len(self.__data) > right and self.__data[right] > self.__data[left]:
                tmp_idx = right
            if self.__data[tmp_idx] > value:
                self.__data[idx] = self.__data[tmp_idx]
                self.__data[tmp_idx] = value
            #else:
                #print(ret)
                #return ret
            idx = tmp_idx
            left = 2 * idx + 1
            right = 2 * idx + 2
            #print(ret)
        #return ret


if __name__ == '__main__':
    heap = Heap()
    for _ in range(10):
        i = random.randint(0, 100)
        print('i is ', i)
        heap.insert(i)
    heap.view()
    #heap.pop()
    heap.remove(1)
    heap.view()
