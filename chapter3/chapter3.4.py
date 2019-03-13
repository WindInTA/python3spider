#!/usr/bin/env python
# @Time : 2019/3/13 15:20
import json
import time

import requests
import re
from requests import RequestException


__author__ = 'Boaz'

# 猫眼猫眼，你终于来了哦




def get_one_page(url):
    '''
    抓取第一页的内容
    :param url:  传入的网址
    :return:
    '''
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) '
                          'AppleWebKit/535.11 (KHTML, like Gecko) '
                          'Chrome/17.0.963.56 Safari/535.11'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile(r'<dd>.*?board-index.*?>(\d+)</i>.*?' +
                         'data-src="(.*?)".*?' +
                         'name"><a.*?>(.*?)</a>.*?' +
                         'star">(.*?)</p>.*?' +
                         'releasetime">(.*?)</p>.*?' +
                         'integer">(.*?)</i>.*?' +
                         'fraction">(.*?)</i>.*?</dd>', re.S
                         )
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5]+item[6]
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8')as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(5):
        main(offset=i*10)
        time.sleep(4)
