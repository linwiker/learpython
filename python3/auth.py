#!/usr/bin/env python
# -*- coding: utf-8 -*-
#从文本取得账号和密码进行用户认证，账号或者密码错误自动退出
import getpass

dict_temp={}
flags = True
f=open("auth.txt","r")
for i in f.readlines():
    data=i.strip().split(";")
    dict_temp[data[0]]={"password":data[1],"count":data[2]}
f.close()
username=input("please input your username:")
if username in dict_temp.keys():
    flags=int(dict_temp[username]["count"])
    while flags < 3:
            passwd=getpass.getpass("please input your password:")
            if passwd==dict_temp[username]["password"]:
                print('wellcome %s' % username)
                break
            else:
                flags += 1
    else:
         print("由于你输入错误次数超过三次，禁止再重新登录")
         dict_temp[username]["count"]=flags
else:
    for i in range(3):
        passwd=getpass.getpass("please input your password:")
    else:
        print("用户名或者密码错误")
list_temp=[]
for i in dict_temp.keys():
    list_temp.append(i+";")
    list_temp.append(dict_temp[i]["password"]+";")
    list_temp.append(str(dict_temp[i]["count"])+"\n")
str_temp="".join(list_temp)
f1=open("auth.txt","w")
f1.write(str_temp)
f1.close()
