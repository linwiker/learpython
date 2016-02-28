#!/usr/bin/env python
# -*- coding: utf-8 -*-
read_me='''first of all, i want maker it clear that i can not clain understand this dishdiahsidas dasdhaisdha isd asd asihdiashdiah'''
dict = {}
sort_list = [('null',0)]
for i in read_me:
    num = read_me.count(i)
    if not i in dict:
        dict[i] = num
        j=0
        while not (num < sort_list[j][1] or j >= len(sort_list)-1):
            j=j+1
        sort_list.insert(j,(i,num))
sort_list.pop()
sort_list.reverse()
for k in range(10):
    print sort_list[k]
