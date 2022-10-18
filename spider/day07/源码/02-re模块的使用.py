#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   02-re模块的使用.py    
# Author :   柏汌  
import re

# match方法进行匹配操作  从头开始匹配
result = re.match('tuling', 'tuling.cn')
# 获取到匹配的结果
info = result.group()
print(info)

