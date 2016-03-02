#/usr/bin/env python
# -*- coding: utf-8 -*-
#把dict_name.txt内容读出来,以name为key输出成字典
dict_temp={}
f=open("dict_name.txt",'r')
for i in f.readlines():
    data=i.strip().split("|")
    dict_temp[data[0]]=[data[1],data[2]]
print(dict_temp)
f.close()
