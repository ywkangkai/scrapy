#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   08-cookiejar.py    
# Author :   柏汌  

import requests


url = "http://www.baidu.com"
#发送请求，获取resposne
response = requests.get(url)  # 3秒钟
print(type(response.cookies))
# 使用dict_from_cookiejar可以重cookie提取出数据
cookie = requests.utils.dict_from_cookiejar(response.cookies)
print(cookie)