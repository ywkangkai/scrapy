#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   03-requests携带headers.py    
# Author :   柏汌  

import requests

# 获取到目标网址
url = 'https://www.baidu.com'


head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
# 发送请求
response = requests.get(url)
# response.encoding = 'utf-8'
# 打印数据
print(response.content.decode('utf-8'))

print(response.request.headers)


