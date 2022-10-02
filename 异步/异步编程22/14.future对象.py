# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 9:14 下午
# @Author  : 顾安
# @File    : 14.future对象.py
# @Software: PyCharm


import asyncio


async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()
    # 创建一个任务[Future对象] 当前没有任何任务
    fut = loop.create_future()
    # 等待任务的最终结果，没有结果则一直等待
    await fut


asyncio.run(main())
