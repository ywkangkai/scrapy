#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   02-豆瓣电影采集.py    
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
# print(html.xpath())
# 获取到href和title的列表
title_list = html.xpath('//div[@id="newscontent"]/div[1]//span[@class="s2"]/a/text()')
print(title_list)
href_list = html.xpath('//div[@id="newscontent"]/div[1]//span[@class="s2"]/a/@href')
# print(href_list)
#
# print(zip(href_list, title_list))
# 组成字典
for href, title in zip(href_list, title_list):
    # print(i)
    item = {}
    item['href'] = href
    item['title'] = title
    print(item)