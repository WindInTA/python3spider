#!/usr/bin/env python
# @Time : 2019/3/14 16:43 
__author__ = 'Boaz'

# 所有的节点
from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//*')  # * 表示所有的节点
print(result)
print('\n'*3)

# 像获取所有的li节点
result1 = html.xpath('//li')
print(result1)
print('\n'*3)

# 获取子节点  例如li的节点下面的a的节点

result2 = html.xpath('//li/a')
print("result2 is", end='')
print(result2)

result3 = html.xpath('//li//a')
print("result3 is ", result3)


result4 = html.xpath('//ul/a')   # 因为a标签不是ul的子标签
print('result4 is', result4)

