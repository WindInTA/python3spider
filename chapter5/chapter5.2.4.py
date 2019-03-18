#!/usr/bin/env python
# @Time : 2019/3/18 11:11
__author__ = 'Boaz'

# 插入数据

import pymysql
data = {
    'id': "20190001",
    'name': 'Bob',
    'age': 20
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
db = pymysql.connect(
    host='localhost', user='root', password='123456', port=3306, db='spiders'
)
cursor = db.cursor()
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(
    table=table, keys=keys, values=values)
print(sql)
try:
    if cursor.execute(sql,tuple(data.values())):
        print('Successful')
        db.commit()
except :
    print('Failed')
    db.rollback()

db.close()
