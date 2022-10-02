# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 10:06 下午
# @Author  : 顾安
# @File    : 9. await-关键字-2.py
# @Software: PyCharm


import asyncio


async def others():
    print('start')
    await asyncio.sleep(2)  # 为了让大家知道如果没有任务切换则只能等待
    print('end')
    return '这是执行完协程函数后所得到的结果'


async def func():
    print('执行协程函数内部代码')
    # 当前await会等待response拿到返回值之后才解堵塞
    # 如果response拿不到返回值则一直堵塞
    response = await others()
    print(response)


asyncio.run(func())
