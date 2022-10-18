#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   06-bs4的基本使用.py    
# Author :   柏汌  
from bs4 import BeautifulSoup
import requests
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
# 格式化输出soup对象
# print(soup.prettify())

# 获取到span标签  find_all方法 传字符串
# span = soup.find_all('span')
# print(span)

# a = soup.find_all('a')
# print(a)

# 传正则表达式
# import re
#
# b_list = soup.find_all(re.compile('^b'))
# for b in b_list:
    # print(b)
# print(b_list)

# 传列表
# data = soup.find_all(['a', 'span'])
# print(data)

# 传keyworld参数
# data = soup.find_all(attrs={'class': 'blue_no_underline'})
# print(data)
