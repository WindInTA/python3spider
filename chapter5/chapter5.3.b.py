#!/usr/bin/env python
# @Time : 2019/3/18 17:37 
__author__ = 'Boaz'

# MongoDB 查询

import pymongo
from bson.objectid import ObjectId

# 创建mongo对象
mongo = pymongo.MongoClient('mongodb://localhost:27017/')

# 选择要连接的数据库
db = mongo.test

# 选择需要的表格
collection = db.students


# 直接查询
result = collection.find_one({'name':'Style'})
print(type(result))
print(result)

# 如果要用mongodb里面的_id的话
result = collection.find_one({'_id':ObjectId('5c8f66770a040015d44ebe25')})
print(result)


# 多行查询
print("多行查询")
results = collection.find({'gender':'female'})
for one in results:
    print(one)

# 条件查询 // 功能查询  我感觉够你喝一壶
print("条件查询")
results = collection.find({'name':{'$regex':'e$'}})
for one in results:
    print(one)

# 计数
print("--------------------------------"*3)
print("计数")
count = collection.find().count()
print(count)


# 偏移
print("--------------------------------"*3)
print("偏移")
results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])


# 更新
print('----------------------------'*3)
print('更新')
condition = {'name': 'Style'}
song = collection.find_one(condition)
song['gender'] = 'male'
result = collection.update(condition,song)
print(result)

# 删除
print('----------------------------'*3)
print('删除')
result = collection.delete_one({'name':'style'})
print(result)
print(result.deleted_count)
