#!/usr/bin/env python
# @Time : 2019/3/16 20:02 
__author__ = 'Boaz'

# 基本CSS选择器


html = '''
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
#CSS 选择器
'''
from pyquery import PyQuery as pq

doc = pq(html)
print(doc('#container'))
print("-------------------")
print(doc('li'))
print(type(doc('#container .list li')))
'''

# 子节点
from pyquery import PyQuery as pq
doc = pq(html)
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li') #找所有子孙节点
print(type(lis))
print(lis)

# 找子节点
lis = items.children('.active')
print(type(lis))
print(lis)

# 找父节点

html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
doc = pq(html)
items = doc('.list')
parent=items.parent()
print(parent)

# 所有祖父
print("祖父节点")
items=doc('.list')
parents = items.parents()
print(parents)

# 单个祖父
print("某个祖父节点")
print(items.parents('.wrap'))

# 兄弟节点
print("兄弟的节点")
li = doc('.list .item-0.active')
print(li.siblings())

# 遍历
print("所有的节点")
doc=pq(html)
li = doc('.item-0.active')
print(li)
print(str(li))

doc = pq(html)
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li, type(li))

#获取信息
#1. 获取属性
print("\n"*3)
print("获取属性")
doc = pq(html)
a = doc('.item-0.active a')
print(a, type(a))
print(a.attr('href'))

#2. 获取文本
print('------------获取文本----------')
doc = pq(html)
a = doc('.item-0.active a')
print(a)
print(a.text())


#    获取内部HTML文本
print('------------获取内部HTML文本----------')
doc = pq(html)
li = doc('.item-0.active')
print(li)
print(li.html())


# 获取多个节点的文本
print('-------------获取多个节点---------------')
li = doc('li')
print(li.html())
print(li.text()) #text()不需要遍历就能获取
print(type(li.text()))


# 节点操作
# addClass 和 removeClass
print('-----------节点操作-----------')
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.remove_class('active')
print(li)
li.add_class('active')
print(li)

# attrt, text ,html
# text ,html 直接对子级下面动手
print("------------增添元素--------------")
html2='''
<ul class="list">
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''

doc = pq(html2)
li = doc('.item-0.active')
print(li)
li.attr('name','link')
print(li)
li.text('changed item!')
print(li)
li.html('<span>changed item?</span>')
print(li)

# remove()
print('---------------remove()-----------')
html3 = '''
<div class="wrap">
    Aloha?
    <p>Today is a boring day!</p>
</div>
'''
doc = pq(html3)
wrap = doc('.wrap')
# 只想选取’Aloha？‘这个句话
wrap.find('p').remove()
print(wrap.text())

# 伪类选择器
# 感觉跟Jquery就时一模一样了嘛
print('---------伪类选择器--------------')
html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
doc = pq(html)
li = doc('li:first-child')
print(li)
print(li.html())
print(li.text())
li = doc('li:last-child')
print(li)
print(li.html())
li = doc('li:nth-child(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
print('---单倍-------')
li = doc('li:nth-child(2n-1)')
print(li)

# 更多的参考css的选择器