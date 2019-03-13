#!/usr/bin/env python
# @Time : 2019/3/12 22:20
__author__ = 'Boaz'


'''
urlib的基本用法记得回去看一下，然后下面都是request的用法
1.cookies
2.user-agent
3.logon
'''

'''
import requests
r = requests.get('https://www.bing.com/')
print(type(r))        # <class 'requests.models.Response'>
print(r.status_code)  # 200
print(type(r.text))   # <class 'str'>
print(r.text)
print(r.cookies)
'''

# GET 请求

'''
import requests
r = requests.get('http://httpbin.org/get')
print(r.text)
'''


# GET 带参数请求
'''
import requests
data={
    'name': 'david',
    'age': 22,
}
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)
print("======转化成JSON=======")
print(r.json())
print(type(r.json()))
'''

# 抓取网页

'''

import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) '
                  'AppleWebKit/535.11 (KHTML, like Gecko) '
                  'Chrome/17.0.963.56 Safari/535.11'
}
r = requests.get('https://www.zhihu.com/explore', headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern,r.text)
print(r.text)
print("=========")
print(titles)
'''


# 抓取二进制数据

'''
import requests

r = requests.get('https://github.com/favicon.ico')
# print(r.text)
# print(r.content)
with open('favicon.ico','wb')as f:
    f.write(r.content)

'''

# 添加headers

'''
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) '
                  'AppleWebKit/535.11 (KHTML, like Gecko) '
                  'Chrome/17.0.963.56 Safari/535.11'
}
r = requests.get('https://www.zhihu.com/explore',headers=headers)
print(r.text)

'''

#POSTS 请求

'''
import requests
data = {'song':'it never rains in California', 'age': '60s'}
r = requests.post('http://httpbin.org/post',data=data)
print(r.text)

'''

#响应
import requests

r = requests.get('http://www.jianshu.com')
print(type(r.status_code),r.status_code)
print(type(r.headers),r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url),r.url)
print(type(r.history),r.history)