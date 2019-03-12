#!/usr/bin/env python
# @Time : 2019/3/7 6:46
__author__ = 'Boaz'

# 解析链接
# urlparse()
'''
from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result)
'''

# urlunparse()
# 实现了URL的构造，长度必须?6
'''
from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

'''

# urlsplit()
# 与urlparse()非常相似，只是不在单独解析params这一部分

'''
from urllib.parse import  urlsplit

result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)
'''

# urljoin()
# 生成另一个合并链接的方法

'''
from urllib.parse import urljoin
print(urljoin('http://www.baidu.com','FAQ.html'))
'''

# urlencode()
# 构造GET请求时候有用

'''

from urllib.parse import urlencode

params = {
    'name':'germey',
    'age':22,
}
base_url = 'http://www.baidu.com?'
url = base_url+urlencode(params)
print(url)

'''


# parse_qs()
# 反序列化

'''
from urllib.parse import parse_qs

query = 'name=germey&age=22'
print(parse_qs(query))
'''



#parse_qsl()
# 把参数转化未元祖组成的列表

'''
from urllib.parse import parse_qsl

query = 'name=germey&age=22'
print(parse_qsl(query))
'''

# quote()把内容转化未URL编码格式，特别是针对中文

'''
from urllib.parse import quote

keyword = "壁纸"
url = 'https://www.google.com/s?wd='+quote(keyword)
print(url)
'''


# unquote() 就是把他还原
from urllib.parse import unquote
url = 'https://www.google.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))

