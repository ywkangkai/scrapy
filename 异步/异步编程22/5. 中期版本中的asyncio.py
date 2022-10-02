# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 9:06 下午
# @Author  : 顾安
# @File    : 5. 中期版本中的asyncio.py
# @Software: PyCharm


import asyncio


async def func1():
    print(1)
    await asyncio.sleep(2)
    print(2)


async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)


async def func3():
    print(5)
    await asyncio.sleep(1)
    print(6)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2()),
    asyncio.ensure_future(func3())
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
