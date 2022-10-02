# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 10:11 下午
# @Author  : 顾安
# @File    : 22.异步操作redis-1.py
# @Software: PyCharm


import asyncio
import aioredis


async def execute(address):
    print('开始执行: ', address)
    # 网络IO 创建redis连接
    redis = await aioredis.create_redis(address)
    # 网络IO 在redis中设置哈希值
    await redis.hmset_dict('car', key1=1, key2=2, key3=3)
    # 网络IO 获取redis中的值
    result = await redis.hgetall('car', encoding='utf-8')
    print(result)
    redis.close()

    # 网络IO 关闭redis连接
    await redis.wait_closed()
    print('结束...')


asyncio.run(execute('redis://127.0.0.1:6379/0'))
