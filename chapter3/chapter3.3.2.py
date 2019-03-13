#!/usr/bin/env python
# @Time : 2019/3/13 13:02 
__author__ = 'Boaz'

# 正则表达式。。。 额，我觉得应该很简单吧，待会写个测试验证一下就🆗了

import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match(r'^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())

print('---------------------------------')
content = 'Hello 1234567 World_This is a regex Demo'
result = re.match(r'^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())

print('--------------------------------')

# 通用匹配

content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match(r'^Hello.*Demo$',content)
print(result)
print(result.group())
print(result.span())

print('----------------------------')

# 贪婪模式
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match(r'^He.*(\d+).*Demo$',content)
print(result)
print(result.group(1))
print(result.span())

print('-------------------------------------')
# 非贪婪模式
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match(r'^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))

print('------------------------------------')
# 如果匹配的字符串在结尾，.*?可能匹配不了任何内容了
import re

content = 'http://weibo.com/comment/kEraCN'
result1 = re.match('http.*?comment/(.*?)', content)
result2 = re.match('http.*?comment/(.*)', content)
print('result1', result1.group(1))
print('result2', result2.group(1))

print('-------------------------------------')

# 修饰符
# 针对语句里面有转义字符的东西

content = '''Hello 1234567 World_This
 is a Regex Demo'''
result = re.match(r'^He.*?(\d+).*?Demo$', content,re.S)
print(result.group(1))

print('---------------------------------------')
print('\n'*3)

# 转义匹配

content = '(百度)www.baidu.com'
result = re.match(r'\(百度\)www\.baidu\.com',content)
print(result)

print('---------------------------------------')
print('\n'*3)

# search() 扫描整个字符串，返回第一个成功的匹配结果
html = '''
<div id='songs-list'>
<h2 class='title>经典老歌</h2>
<p class='introduction'>
经典老歌列表
</p>
<ul id='list' class='list-group'>
<li data-view='2'>一路上有你</li>
<li data-view='7'>
<a href='/2.mp3' singer='任贤齐'>沧海一声笑</a>
</li>
<li data-view="4" class='active'>
<a href='/3.mp3' singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a><li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>
'''
result = re.search(r'<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result:
    print(result.group(1), result.group(2))
print("OK")


print('---------------------------------')
print('\n'*2)


# findall() 寻找所有的匹配到的结果
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print(results)



# sub() 用来修改文本

import re

content= 'Wewillmeetyouin2022!'
content = re.sub('\d+','2024',content)
print(content)