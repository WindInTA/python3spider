#!/usr/bin/env python
# @Time : 2019/3/19 4:20 
__author__ = 'Boaz'

# 传说中的redis

from redis import StrictRedis

redis = StrictRedis(host='localhost',port=6379, db=0, password='12345')
redis.set('name', 'Bob')
print(redis.get('name'))
