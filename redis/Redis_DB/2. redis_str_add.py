# -*- coding: utf-8 -*-
# @Time    : 2022/9/7 10:04 下午
# @Author  : 顾安
# @File    : 2. redis_str_add.py
# @Software: PyCharm


import redis


# 1. 连接数据库
redis_cli = redis.Redis(host='localhost', port=6379, db=1)

# 2. 在redis中存储一个字符串
result = redis_cli.set('name', '夏洛')

# 3. 打印结果
print(result)
