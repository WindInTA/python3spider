#!/usr/bin/env python
# @Time : 2019/3/6 17:40
__author__ = 'Boaz'


import urllib.request
import urllib.parse
import urllib.error
from urllib import request, parse


# urlopen()
'''
response = urllib.request.urlopen('http://www.python.org')
print(response.read().decode("utf-8"))
'''

'''
# response = urllib.request.urlopen('http://www.python.org')
# print(type(response))
'''

'''
response = urllib.request.urlopen('http://www.python.org')
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
'''

# 传入 data 参数  (是用表格的方式来传输的)
'''
data = bytes(urllib.parse.urlencode({'word': 'Aloha'}), encoding='utf-8')
response = urllib.request.urlopen(
    "http://httpbin.org/post", data=data
)
print(response.read())
'''


# timeout 参数  (如果超时就会报错)
"""
response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.01)
print(response.read())
"""

# 设置超时时间，如果长时间没有响应就跳过
'''
import socket

try:
    response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.001)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("TIME OUT")

'''

# ######Request

# 用的是一个request的对象来获得
'''
request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
'''

# 传入多个参数来看看
'''
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0(compatible,MSIE 5.5;Windows NT)',
    'host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

'''

# 验证 我没有网站可以测试，所以就不错了


# 代理  给爬虫用的    --结果目标计算机积极拒绝，我也是醉了。。。。
'''
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743',
})

opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.ping.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
'''

# Cookies
import http.cookiejar,urllib.request

# 感觉结果都呗改了很多很多
'''
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in response:
    print(item)
'''

filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)
