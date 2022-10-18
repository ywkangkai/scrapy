#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   02-requests获取百度图标.py    
# Author :   柏汌  

import requests

# 获取到url地址
url = 'https://www.baidu.com/img/pc_79bff59263430e2e42693b50cf376490.png'
response = requests.get(url)
print(response.content)
with open('百度.png', 'wb')as f:
    f.write(response.content)