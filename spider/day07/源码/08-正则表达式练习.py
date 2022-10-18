#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   08-正则表达式练习.py    
# Author :   柏汌  

import requests
import re

# 获取到网址
url = 'https://www.qqtxt.cc/list/1_1.html'
# 发送请求
response = requests.get(url)
response.encoding = 'gbk'
# print(response.text)
data = re.findall('<li><span class="s2">《<a href="(.*?)" target="_blank">(.*?)</a>》</span>', response.text, re.S)
print(data)
# for i in data:
#     print(i)