#!/usr/bin/env python
# -*- coding: utf-8 -*-
#给文件的内容每一行添加一个行号
f1 = open('hello.txt')
cNames = f1.readlines()
for i in range(len(cNames)):
    cNames[i]= str(i+1)+ ' ' + cNames[i]
f1.close()
f2 = open('test','w')
f2.writelines(cNames)
f2.close()
    
