#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   06-匹配分组.py    
# Author :   柏汌  

import re

# 实例： |
# 需求：在列表中["apple", "banana", "orange", "pear"]，匹配apple和pear

# fruit_list = ["apple", "banana", "orange", "pear"]
#
# # 遍历列表
# for i in fruit_list:
#     ret = re.match('apple|pear', i)
#     if ret:
#         print('%s是我想吃的水果' % ret.group())
#     else:
#         print("%s不是我想吃的水果"% i)

# 实例：()
# 需求：匹配出163、126、qq等邮箱
# ret = re.match('[A-Za-z0-9_]{4,20}@(163|qq|126|sin)(\.com)', 'hello@sin.com')
# print(ret.group(2))

# 实例：\num
# 需求：匹配出hh
# str1 = '<div>hh</div>'
# ret = re.match('<([A-Za-z1-6]+)>.*</\\1>', str1)
# print(ret.group(0))

# 实例：(?p)  (?p=name)
# str1 = '<html><h1>www.tuling.cn</h1></html>'
# ret = re.match('<(?P<213>[A-Za-z1-6]+)><(?P<name2>[A-Za-z1-6]+)>.*</(?P=name2)></(?P=213)>', str1)
# print(ret.group())




