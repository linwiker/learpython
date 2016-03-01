#!/usr/bin/env python
# -*- coding: utf-8 -*-
#用户认证，账号或者密码错误自动退出
import getpass

username=input("please input your username:")
if username =='wiker':
    for i in range(3):
        passwd=getpass.getpass("please input your password:")
        if passwd=='12345':
            print('wellcome %s' % username)
            break
    else:
        print("用户名或者密码错误")
else:
    for i in range(3):
        passwd=getpass.getpass("please input your password:")
    else:
        print("用户名或者密码错误")
