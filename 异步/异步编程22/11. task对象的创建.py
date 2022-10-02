# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 8:28 下午
# @Author  : 顾安
# @File    : 11. task对象的创建.py
# @Software: PyCharm


import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '这是一个返回值'


async def main():
    print('开始任务...')
    # 创建task对象，将当前的func任务添加到事件循环中
    task_1 = asyncio.create_task(func())
    task_2 = asyncio.create_task(func())
    print('任务结束...')

    # 当执行某些协程遇到IO操作时，会自动切换执行其他任务
    # 此处的await是等待相对应的协程全部执行完毕并获取结果
    result_1 = await task_1
    result_2 = await task_2
    print(result_1, result_2)


asyncio.run(main())
