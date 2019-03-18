#!/usr/bin/env python
# @Time : 2019/3/18 17:27 
__author__ = 'Boaz'

# MongoDB 存储

import pymongo
client = pymongo.MongoClient(host='localhost',port=27017)

# 或者
# client =pymongo.MongoClient('mongodb://localhost:27017/')

# 指定连接某个数据库
db = client.test
# db = client['test']

collection = db.students
# collection = db['students']

student = {
    'id':'20190001',
    'name':'Blank Space',
    'gender':'female'
}

result = collection.insert_one(student)
print(result)

student1 = {
    'id': '20190002',
    'name': 'Style',
    'gender': 'female'
}

student2 = {
    'id': '20190003',
    'name': 'RED',
    'gender': 'female'
}

result2 = collection.insert_many([student1,student2])
print(result2)