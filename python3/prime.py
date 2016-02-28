#!/usr/bin/python
# -*- coding: utf-8 -*-
#统计素数个数
temp_list=[2,3,4,5,6,7]
i=0
for n in temp_list:
	for x in range(2,n):
		if n%x==0:
			break
	else:
		i+=1
print(i)
