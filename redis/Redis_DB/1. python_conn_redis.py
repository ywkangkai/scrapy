# -*- coding: utf-8 -*-
# @Time    : 2022/9/7 10:00 下午
# @Author  : 顾安
# @File    : 1. python_conn_redis.py
# @Software: PyCharm

"""
如何连接redis

    pip install redis
"""

import redis

redis_cli = redis.Redis(host='localhost', port=6379, db=0)

print(redis_cli)
