#!/usr/bin/env python

f=open('access.log','r')
d = {}
for line in f.read().split('\n'):
    arr = line.split()
    if len(arr) < 9:
        continue
    tup1=arr[8],arr[6],arr[0]
    d[tup1]= d.get(tup1,0)+1
l1=d.items()
for i in  range(len(l1)-1):
    for j in range(len(l1)-i-1):
        if l1[j][1] > l1[i+1][1]:
            l1[j],l1[j+1]=l1[j+1],l1[j]
l1.reverse()
for k in range(10):
    print l1[k][0],l1[k][1]
