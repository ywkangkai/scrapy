#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   10-retry模块使用.py    
# Author :   柏汌
import requests
from retrying import retry

# 最大的重试次数3， 超过3次报错

@retry(stop_max_attempt_number=3)
def reques_url(url):
    # 超时重试的代码
    print(111)
    response = requests.get(url, timeout=3)
    return response

def parse_url(url):
    try:
        res = reques_url(url)
    except Exception as e:
        print(e)
        res = None
    return res


print(parse_url('http://www.baidu.com'))


