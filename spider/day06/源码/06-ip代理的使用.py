#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   06-ip代理的使用.py    
# Author :   柏汌  

import requests

proxies = {
    'http': "http://58.20.184.187:9091",
}

url = 'http://httpbin.org/ip'
response = requests.get(url, proxies=proxies, timeout=2)
print(response.text)

