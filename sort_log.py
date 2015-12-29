#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 统计nginx的access_log日志的状态+url+ip地址的最多的十次
f=open('access.log','r')
d = {}
def sort_fun(arr):
    return arr[1]
for line in f.read().split('\n'): #把从文件中读取的条目以\n为分隔符生成一个大的list,并且每次line从这个list取出一个字符串
    arr = line.split() #把取出来的字符串以空格为分隔符生成list
    if len(arr) < 9: #过滤不符合规范的日志
        continue
    temp_tup=(arr[8],arr[6],arr[0]) #以生成list的第8\6\0字符生成元组
    d[temp_tup]= d.get(temp_tup,0)+1 #以上面的元组为key生成字典，这样就统计出来这个元组的个数了
temp_list=d.items() #把字典d转换为list
ls=sorted(temp_list,key=sort_fun)
ls.reverse()
for k in range(10):
    print ls[k][0],ls[k][1]
