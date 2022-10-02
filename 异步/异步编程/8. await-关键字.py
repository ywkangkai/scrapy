# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 10:01 下午
# @Author  : 顾安
# @File    : 8. await-关键字.py
# @Software: PyCharm


import asyncio


async def func():
    print('开始协程任务...')
    # 模拟IO等待 如果当前有其他任务则切换
    response = await asyncio.sleep(2)
    print('任务结束: ', response)


asyncio.run(func())
