#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   01-requests发送请求.py    
# Author :   柏汌  


# 下载   pip install requests
"gbk     utf-8"
import requests

# 获取到目标网址
url = 'https://www.baidu.com'

# 发送请求
response = requests.get(url)
# response.encoding = 'utf-8'
# 打印数据
print(response.content.decode('utf-8'))
# print(response.text)
# print(response.json())

# 查看响应头  查看状态码
# print(response.status_code)
# print(response.headers)
# print(response.request.headers)
# print(response.cookies)


