#!/usr/bin/env python
# encoding='utf-8'
# @Time : 2019/3/17 20:04 
__author__ = 'Boaz'

# JSON文件存储

import json

strtest = '''
[{
        "name" : "Bob",
        "gender" :"male",
        "birthday" : "1992-10-23"
},{
        "name" : "Selina",
        "gender" :"female",
        "birthday" : "1995-11-23"
}
]
'''


# strtest='''
# {"http://example.org/about": {"http://purl.org/dc/terms/title": [{"type": "literal", "value": "Anna's Homepage"}]}}
# '''


# 原来最后一行不能有逗号，以后该加就加，不该加就不要乱加
print(type(strtest))
data = json.loads(strtest)
print(data)
print(type(data))
print(data[0]['name'])
with open('data.json', 'w') as file:
    file.write(json.dumps(data))

# 使用中文的话
data2=[{
    'name':'王伟',
    'gender':'男',
    'birthday': '1992-10-18',
}]
with open('data.json','a') as file:
    file.write(json.dumps(data,indent=2,ensure_ascii=False))