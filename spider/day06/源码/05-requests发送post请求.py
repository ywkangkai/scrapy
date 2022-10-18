#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   05-requests发送post请求.py    
# Author :   柏汌  

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
data = {
    'column': 'szse_latest',
    'pageNum': '1',
    'pageSize': '30',
    'sortName': '',
    'sortType': '',
    'clusterFlag': 'true',
}

# 获取到url地址
url = 'http://www.cninfo.com.cn/new/disclosure'
# 发送请求
response = requests.post(url, headers=headers, data=data)
print(response.json())
