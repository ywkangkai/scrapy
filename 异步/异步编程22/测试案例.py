# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 10:41 下午
# @Author  : 顾安
# @File    : 测试案例.py
# @Software: PyCharm


import asyncio


async def func():
    # print(1)
    await asyncio.sleep(2)
    # print(2)
    return '这是一个返回值'


async def main():
    tasks_list = [
        asyncio.create_task(func()),
        asyncio.create_task(func())
    ]

    result, pending = await asyncio.wait(tasks_list)
    # 这里的循环和异步循环没有关系
    for item in result:
        print(item.result())


asyncio.run(main())

