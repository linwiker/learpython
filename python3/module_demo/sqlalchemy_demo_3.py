#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:redhat@127.0.0.1:3306/python3", max_overflow=5)
Base = declarative_base()

#定义表结构
class Users_demo(Base):
    __tablename__ = 'users_demo'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

#寻找Base的所有子类，按照子类的结构在数据库中生成所有对应的数据表信息，简单点就是生成上面定义的表
Base.metadata.create_all(engine)

#创建连接信息进行数据库对数据库表进行操作
Session = sessionmaker(bind=engine)
session = Session()

#增加操作
u = Users_demo(id=1, name='wiker')
session.add(u)
session.add_all([Users_demo(id=2, name='zhou'), Users_demo(id=3, name='linwiker')])
session.commit()

#删除操作
session.query(Users_demo).filter(Users_demo.id > 2).delete()
session.commit()

#修改操作,把id大于2的name更改为TT
session.query(Users_demo).filter(Users_demo.id > 2).update({'name':'TT'})
session.commit()

#查询操作
ret1 = session.query(Users_demo).filter_by(name='wiker').first()
ret2 = session.query(Users_demo).filter_by(name='wiker').all()
ret3 = session.query(Users_demo).filter(Users_demo.name.in_(['wiker', 'zhou'])).all()
ret4 = session.query(Users_demo).order_by(Users_demo.id).all()
ret5 = session.query(Users_demo).order_by(Users_demo.id)[1:3]
session.commit()

