#!/usr/bin/python
# -*- coding: utf-8 -*-
#filename delrepeat.py
#移除重复的元素，只保留第一个，并且保持列表原来的次序不变
lista=[1,3,2,4,3,4,2,5,5,7]
lista.reverse()
for i in lista:
	if lista.count(i) >1:
		lista.remove(lista[i])
lista.reverse()	
print(lista)
