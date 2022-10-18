#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   05-单独标签的提取.py    
# Author :   柏汌  

from lxml import etree
import requests

# 获取资源地址
url = 'https://www.qqtxt.cc/xuanhuan/'
response = requests.get(url)
response.encoding = 'gbk'
# print(response.text)
# 转换字符串数据类型为元素对象
html = etree.HTML(response.text)
li_list = html.xpath('//div[@class="l"]/ul/li')
for li in li_list:
    # print(li)
    item = {}
    item['title'] = li.xpath('./span[@class="s2"]/a/text()')[0] if len(li.xpath('./span[@class="s2"]/a/text()')) > 0 else None
    item['href'] = li.xpath('./span[@class="s2"]/a/@href')[0] if len(li.xpath('./span[@class="s2"]/a/@href')) > 0 else None
    print(item)


