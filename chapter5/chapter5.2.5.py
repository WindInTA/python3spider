#!/usr/bin/env python
# @Time : 2019/3/18 17:17 
__author__ = 'Boaz'

# 查询数据

import pymysql

db = pymysql.connect(
    host='localhost', user='root', password='123456', port=3306, db='spiders'
)
cursor = db.cursor()
sql = 'SELECT * FROM students WHERE age >=19'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:',one)
    results = cursor.fetchall()
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')

db.close()