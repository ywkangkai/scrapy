#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   04-发送携带参数得 请求.py    
# Author :   柏汌  

import requests

# url = 'https://www.baidu.com/s'
#
# head = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
# }
# kw = {
#     'wd':'python',
# }
#
#
# response = requests.get(url, params=kw, headers=head)
# print(response.text)

url = 'https://www.baidu.com/s?wd=python'
response = requests.get(url)

