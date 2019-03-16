#!/usr/bin/env python
# @Time : 2019/3/16 0:40 
__author__ = 'Boaz'

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">
        Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
        <p class="story">...</p>
"""
from bs4 import BeautifulSoup

#  嵌套选择
soup = BeautifulSoup(html, 'lxml')
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)

# 关联选择
html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
    <p class="story">
        Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
    <p class="story">...</p>
"""
soup = BeautifulSoup(html,'lxml')
print(soup.p.contents)

print("也可以用children")
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)

# 父节点和祖先节点
print("========")
html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
    <p class="story">
        Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
        and they lived at the bottom of a well.</p>
    <p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.a.parent)
print("祖先的")
print("\n"*3)
print(soup.a.parents)
print(list(enumerate(soup.a.parents)))

# 兄弟节点
html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
    <p class="story">
        Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1"><span>Elise</span></a>,
        and they lived at the bottom of a well.
        <a href="http://example.com/elsie" class="sister" id="link1"><span>Lacie</span></a>,
        <a href="http://example.com/elsie" class="sister" id="link1"><span>Tillie</span></a>,

    </p>
    <p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
print('Next sibling', soup.a.next_sibling)
print('Prev Sibling', soup.a.previous_sibling)
print('Next Siblings', list(enumerate(soup.a.next_siblings)))
print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))


# 提取信息
print("\n"*3)
html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
    <p class="story">
        Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Bob</a>,
        and they lived at the bottom of a well.
        <a href="http://example.com/elsie" class="sister" id="link1">Lacie</a>,

    </p>
"""
soup = BeautifulSoup(html,'lxml')
print("Next Sibling:")
print(type(soup.a.next_sibling))
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.a.parents))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])