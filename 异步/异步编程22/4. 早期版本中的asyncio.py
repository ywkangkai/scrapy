# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 8:51 下午
# @Author  : 顾安
# @File    : 4. 早期版本中的asyncio.py
# @Software: PyCharm


import asyncio


@asyncio.coroutine
def func1():
    print(1)
    yield from asyncio.sleep(2)
    print(2)


@asyncio.coroutine
def func2():
    print(3)
    yield from asyncio.sleep(2)
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
