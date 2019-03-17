#!/usr/bin/env python
# @Time : 2019/3/17 20:53
__author__ = 'Boaz'

# CSV 文件存储

import csv
# with open('data.csv', 'w', encoding='utf-8')as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['1001', 'Mike', 20])
#     writer.writerow(['1002', 'Bob', 22])
#     writer.writerow(['1003', 'Jordan', 21])
#     writer.writerow(['1004', '猫', 46])


# 爬虫爬去的都是结构化的数据，一般用字典来表示
with open('data.csv', 'w', encoding='utf-8',newline='')as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writerow({'id':'1004', 'name':'Mike', 'age':20})
    writer.writerow({'id':'1005', 'name':'Mike', 'age':20})
    writer.writerow({'id':'1006', 'name':'Mike', 'age':20})


# 读取 CSV文件
with open('data.csv','r',encoding="utf-8")as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)