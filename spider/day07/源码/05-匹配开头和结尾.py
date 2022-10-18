#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   05-匹配开头和结尾.py    
# Author :   柏汌  

import re

# 实例：^ 以某某开头
# 需求：匹配以数字开头的数据
# ret = re.match('^\d.*', 'a45hkjahsdfjk')
# print(ret.group())

# 实例： $ 以特定的数据结尾
# 需求：匹配以数字结尾的数据
# ret = re.match('.*\d$', 'asdjkyfhjksdh')
# print(ret.group())
# 需求: 匹配以数字开头中间内容不管以数字结尾
# ret = re.match('^\d.*\d$', '143iuhdui9\n')
# print(ret.group())
# 需求: 第一个字符除了aeiou的字符都匹配
# ret = re.match('[^aeiou]', 'e')
# print(ret.group())