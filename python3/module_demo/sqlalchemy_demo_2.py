#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import  create_engine, Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

#创建user和color表
user = Table('user', metadata, Column('id', Integer, primary_key=True), Column('name', String(20)),)
color = Table('color', metadata, Column('id', Integer, primary_key=True), Column('name', String(20)),)

#使用pymysql进行数据库连接
engine = create_engine("mysql+pymysql://root:redhat@127.0.0.1:3306/python3", max_overflow=5)

metadata.create_all(engine) #执行创建动作

#创建engine的连接
conn = engine.connect()

#创建sql语句
conn.execute(user.insert(), {'id':7, 'name':'wiker'})
conn.close()
