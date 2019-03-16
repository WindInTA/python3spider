#!/usr/bin/env python
# @Time : 2019/3/16 15:48 
__author__ = 'Boaz'

# 使用pyquery

# 1. 字符串初始化

html = '''
<div>
<ul>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
print(doc('li'))


# 2.URL初始化
doc = pq(url='https://cuiqingcai.com')
print(doc('title'))

#3.文件初始化
doc = pq(filename='test.html')
print(doc('li'))