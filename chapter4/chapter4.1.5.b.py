#!/usr/bin/env python
# @Time : 2019/3/14 17:00 
__author__ = 'Boaz'

# 父节点， 属性匹配，文本获取，属性获取，属性多值匹配，多属性匹配，按序选择，节点轴选择

from lxml import etree

# 可以用 .. 来获取父节点n
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

# 也可以用 parent:: 来获取父节点
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

# 属性匹配
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]')
print(result)

# 获取文本 两种方法
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]//text()')
print(result)

# 获取属性
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)

# 属性多值匹配   在有的class的属性值很多的时候才能配置好，就这样吧。
text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[@class="li"]/a/text()')
print(result,"没有显示结果")
result = html.xpath('//li[contains(@class,"li")]/a/text()')
print(result)


# 多个属性匹配
text = '''
<li class="li li-first" name="item"><a href="link.html">first item多个值</a></li>

'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(result)