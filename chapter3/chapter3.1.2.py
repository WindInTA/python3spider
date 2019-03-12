#!/usr/bin/env python
# @Time : 2019/3/7 3:44 
__author__ = 'Boaz'

# 处理异常

# urllib 的error 模块定义了由request模块产生的异常。

# URLError

'''
from urllib import request,error
try:
    response = request.urlopen('http://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason)
'''

# HTTPError
'''
from urllib import request,error
try:
    response = request.urlopen('http://cuiqingcai.com/index.html')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
'''

# 由于URLError是HTTPError的父类，先捕获之类，在捕获父类
'''
from urllib import request, error
try:
    response = request.urlopen('http://cuiqingcai.com/index.html')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')
'''


# 有时候返回的错误不一定是字符串，也可能是对象
import socket
import urllib
from urllib import request,error


try:
    response = request.urlopen('http://www.baidu.com',timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')