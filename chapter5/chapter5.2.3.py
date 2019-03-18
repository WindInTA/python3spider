#!/usr/bin/env python
# @Time : 2019/3/17 23:50
__author__ = 'Boaz'

# 创建表格
import pymysql
db = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    port=3306,
    db='spiders'
)
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students' \
      '(id VARCHAR(225) NOT NULL, ' \
      'name VARCHAR (225) NOT NULL,' \
      'age INT NOT NULL ,' \
      'primary key(id)'
cursor.execute()
db.close()

