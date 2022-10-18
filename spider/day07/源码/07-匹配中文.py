#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   07-匹配中文.py    
# Author :   柏汌  

import re
title = '你好，hello，世界'

ret = re.findall('[\u4e00-\u9fa5]', title)
print(ret)
