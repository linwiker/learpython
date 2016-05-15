#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:redhat@127.0.0.1:3306/python3", max_overflow=5)

engine.execute("insert into UserInfo (id, name) values(5,'zq')")

result = engine.execute('select * from UserInfo')
print(result.fetchall())
