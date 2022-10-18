#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   07-bs4css选择器.py    
# Author :   柏汌  

from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import random

#print(UserAgent().random)


# 获取到网址
url = 'http://ip.yqie.com/ipproxy.htm'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
# print(response.text)
# 创建BeautifulSoup对象
soup = BeautifulSoup(response.text, 'lxml')

# 1.通过标签选择器查找
# title = soup.select('title')
# print(title)
# a = soup.select('a')
# print(a)

# 2类选择器
# class_data = soup.select('.divcenter')
# print(class_data)

# 带空格的类如何处理 中间的空格换成点
# class_data = soup.select('.adsbygoogle')
# print(class_data)

# id选择器
# id_data = soup.select('#footercopyright')
# print(id_data)

# 层级选择器
# div_data = soup.select('div .navigationlinknoline') #找到div标签中带有navigationlinknoline属性的标签
# div_data2 = soup.select('div .navigationlinknoline img')
# print(div_data)

# 属性选择器
tr_list = soup.select('tr[align="center"]')
#tr_list = soup.select('tr[align="center"] th')
#print(tr_list)

# 获取到文本内容  get_text()
# title = soup.select('title')
# print(title[0].get_text())

# 伪类选择器
# addrs = soup.select('tr td:nth-child(3)')
# print(addrs)
# for add in addrs:
#     print(add.get_text())

# 获取标签属性  get('属性名字')
# a_href = soup.select('ul a[class="blue_no_underline"]')
# print(a_href)
# for a in a_href:
#     print(a.get('href'))


# 获取标签属性  get('属性名字')
a_href = soup.select('ul .navigationlink')
print(a_href)
for a in a_href:
    print(a.get('target'))