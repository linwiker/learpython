#!/usr/bin/env python
# -*- coding: utf-8 -*-
#三级菜单，依次进入各级子菜单，以中国省市做演示
dict_temp={"山东":["济南","青岛","临沂"],"江苏":["南京","南通","徐州"],"河南":["洛阳","开封","新乡"]}
dict_sdcity={"济南":["历城区","槐荫区","历下区"],"青岛":["四方","莱西","胶州"],"临沂":["郯城","苍山","沂水"]}
data=input("please input your province(山东、江苏、河南): ")
print(dict_temp[data])
while data=="山东":
    sddata=int(input("please input your city num(0,1,2):"))
    if dict_temp[data][sddata] in dict_sdcity.keys():
        print(dict_sdcity[dict_temp[data][sddata]])
        break
    else:
        print("input error")
    
        
        
        
    

