#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   02-json数据存储.py    
# Author :   柏汌  

# 获取到4399最新小游戏
#
# 	网址：https://www.4399.com/flash/


import requests
from lxml import etree
import json

url = 'https://www.4399.com/flash/'

headers = {

}

response = requests.get(url, headers=headers)
response.encoding = 'gbk'

html = etree.HTML(response.text)
li_list = html.xpath('//ul[@class="n-game cf"]/li')
data_list = []
for li in li_list:
    item = {}
    item['href'] = li.xpath('./a/@href')[0]
    item['title'] = li.xpath('./a/b/text()')[0]
    print(item)
    data_list.append(item)
with open('data.json', 'w', encoding='utf-8')as f:
    f.write(json.dumps(data_list, ensure_ascii=False, indent=5))

