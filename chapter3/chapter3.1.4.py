#!/usr/bin/env python
# @Time : 2019/3/12 22:13 
__author__ = 'Boaz'

'''
利用urllib的robotparser模块来分析Robots的协议
'''

from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robotx.txt')
rp.read()
print(rp.can_fetch('*', 'https://www.jianshu.com/p/54ef5728e097'))
print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))