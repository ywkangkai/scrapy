#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   04-匹配多个字符.py    
# Author :   柏汌  

import re

# 实例  ：*  匹配0次或者无限次
#需求：匹配出一个字符串第一个字母为大写字符，后面都是小写字母并且这些小写字母可 有可无
ret = re.match('[A-Z][a-z]*?', 'MasdfasNdfssdfgsdfgdfgd柏汌')
print(ret.group())

# 实例： + 匹配前面的字符出现1次或者无限次
# 需求：匹配一个字符串，第一个字符是t,最后一个字符串是o,中间至少有一个字符

# ret = re.match('t.+o', 'toooooox\noo')
# print(ret.group())

# 实例： ? 0次或者一次
# 需求：匹配出这样的数据，但是https 这个s可能有，也可能是http 这个s没有
# ret = re.match('https?', 'https')
# print(ret.group())


# 实例：{5} {8, 20}，匹配括号里出现的次数
# 需求：匹配出，8到20位的密码，可以是大小写英文字母、数字、下划线
ret = re.match('[A-Z]{2}[0-9a-zA-Z_]{8,20}', 'ZZa123AfAshu13yiuh4')
print(ret.group())
