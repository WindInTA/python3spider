#!/usr/bin/env python
# @Time : 2019/3/14 17:55 
__author__ = 'Boaz'

# 按序选择
from lxml import etree

text = '''

<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>

'''

html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')
print(result)
print("可以显示first嘛？？？")
result = html.xpath('//li[first()]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)

print("=================\n"*3)

# 节点轴选择
text2 = '''

<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>

'''
html = etree.HTML(text2)
result = html.xpath("//li[1]/ancestor::*")
print(result)
result = html.xpath("//li[1]/ancestor::div")
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/child::*')   # 子节点
print(result)
result= html.xpath("//li[1]/descendant::span")
print(result)
result = html.xpath("//li[1]/following-sibling::*")  # 同一级的属性节点
print(result)