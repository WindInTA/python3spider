#!/usr/bin/env python
# @Time : 2019/3/16 14:16 
__author__ = 'Boaz'


html='''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>   
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.find(name='ul'))
print(type(soup.find(name='ul')))
print(soup.find(class_='list'))



# CSS 选择器
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))

print('\n'*3)
# 嵌套选择
for ul in soup.select('ul'):
    print(ul.select('li'))

print('\n'*3)
# 获取属性
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])


# 获取文本
for li in soup.select('li'):
    print('GET Text', li.get_text())
    print('String:', li.string)