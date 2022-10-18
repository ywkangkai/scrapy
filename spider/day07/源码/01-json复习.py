#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   01-json复习.py    
# Author :   柏汌  

import json

# python 数据转成json字符串
a = {11:222, 'aa': 33}

json_1 = json.dumps(a)
print(json_1)

# json.loads() 将json数据转换成字典数据



