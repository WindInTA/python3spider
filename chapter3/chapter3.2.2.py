#!/usr/bin/env python
# @Time : 2019/3/13 12:18 
__author__ = 'Boaz'

# 接下来说的是高级用法。我也不会知道咋样，就这么说了，喵。。

# 文件上传
'''
import requests
files={
    'file': open('favicon.ico', 'rb'),
}

r = requests.post('http://httpbin.org/post',files=files)
print(r.text)

'''

# Cookies

'''

import requests

r = requests.get('https://www.baidu.com')
print(r.cookies)
for key,value in r.cookies.items():
    print(key +'='+value)

'''

# Session 维持

'''
import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
'''

# SSL 证书验证

'''
import requests

response = requests.get('https://www.12306.cn')
print(response.status_code)
# 蛤，12306安装了SSL了？？？真的舍得哦
'''

# 代理设置

'''
import requests

proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}
requests.get('https://www.taobao.com', proxies=proxies)
# 没钱买代理，就先在这里放着吧
'''

# 超时设置

'''
import requests

r = requests.get('https://www.taobao.com', timeout=1)
print(r.status_code)

r = requests.get('https://www.google.com', timeout=None)

'''

# 7. 身份认证

'''
import requests
from requests.auth import HTTPBasicAuth

r = requests.get('http://www.baidu.com',auth=HTTPBasicAuth('username','password'))
print(r.status_code)

'''

# 8. Prepared Request

from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name':'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) '
                  'AppleWebKit/535.11 (KHTML, like Gecko) '
                  'Chrome/17.0.963.56 Safari/535.11'
}
s = Session()
req = Request('POST',url,data=data,headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
