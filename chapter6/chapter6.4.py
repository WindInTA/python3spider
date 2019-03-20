#!/usr/bin/env python
# @Time : 2019/3/20 10:12
import os
import re
from hashlib import md5
from multiprocessing.pool import Pool

from requests import codes
__author__ = 'Boaz'

# 今日头条

import requests
from urllib.parse import urlencode


def get_page(offset):
    params = {
        'aid': "24",
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
    }
    base_url = 'https://www.toutiao.com/api/search/content/?keyword=%E8%A1%97%E6%8B%8D'
    url = base_url + urlencode(params)
    try:
        response = requests.get(url)
        print(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def get_image(json):
    if json.get('data'):
        items = json.get('data')
        for item in items:
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                # origin_image = re.sub("list","")
                origin_image = re.sub("list", "origin", image.get('url'))
                yield {
                        'image':  origin_image,
                    'title': title
                }


# def get_image(json):
#     if json.get('data'):
#         data = json.get('data')
#         for item in data:
#             if item.get('cell_type') is not None:
#                 continue
#             title = item.get('title')
#             images = item.get('image_list')
#             for image in images:
#                 origin_image = re.sub("list", "origin", image.get('url'))
#                 yield {
#                     'image':  origin_image,
#                     # 'iamge': image.get('url'),
#                     'title': title
#                 }


def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir('jiepai/'+item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == codes.ok:
            file_path = '{0}/{1}.{2}'.format(item.get('title'),
                                             md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image, item %s' % item)


def main(offset):
    json = get_page(offset)
    for item in get_image(json):
        print(item)
        save_image(item)


GROUP_START = 0
GROUP_END = 7

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
