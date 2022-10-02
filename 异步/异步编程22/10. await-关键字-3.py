# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 10:11 下午
# @Author  : 顾安
# @File    : 10. await-关键字-3.py
# @Software: PyCharm


import asyncio


async def others():
    print('start')
    await asyncio.sleep(2)
    print('end')
    return '这是执行完协程函数后所得到的结果'


async def func():
    print('执行协程函数内部代码')
    # 在当前创建了一个task对象 task对象会自动将others协程对象放入到事件循环中进行执行
    response_1 = asyncio.create_task(others())
    # 同理
    response_2 = asyncio.create_task(others())
    done, pending = await asyncio.wait([response_1, response_2])
    print(done)


# 当前事件循环中一共有几个任务 这个地方有三个任务
# 当前的func是一个协程对象 如果将一个协程对象直接放入到事件循环中则自动创建一个task对象
asyncio.run(func())
