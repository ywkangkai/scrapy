#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   03-单个字符匹配.py    
# Author :   柏汌  


import re  # 这个是正则表达式的模块


# 实例：.
# ret = re.match('柏.', '柏你')
# print(ret.group())

# 实例：[]

# str1 = '2hello'
# ret = re.match('[0123456789]hello', str1)
# print(ret.group())

# 实例：\d
# ret = re.match('嫦娥\d号', '嫦娥52号')
# print(ret.group())

# 实例：\D

# ret = re.match('\D', '\r52号')
# print(ret.group())

# 实例：\s  匹配空白
# ret = re.match('hello\sworld', 'hello\nworld')
# print(ret.group())

# 实例：\s  匹配非空白
# ret = re.match('hello\Sworld', 'hello\nworld')
# print(ret.group())


# 实例：\w  匹配a-z、 A-Z、 0-9、’_‘ 中文
# ret = re.match('\w', '_')
# print(ret.group())

# 实例：\W  匹配非a-z、 A-Z、 0-9、’_‘ 中文
# ret = re.search('\W', '12346734657aksdjfghjksdgh')
# print(ret.group())

# findall用法 查找所以匹配到的数据
# res = re.findall("\d","tuling")
# print(res)

# sub 替换数据  第一个参数是匹配的语法  第二个参数是替换的结构  第三个需要替换的字符串
# res = re.sub("\d","_","tu1ling2")
# print(res)

# compile  re.S修饰符
# p = re.compile('\d', re.S)
# res = p.findall('tu1ling2')
# print(res)

ret = re.match('.', '\n', re.S)
print(ret.group())