# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 9:49 下午
# @Author  : 顾安
# @File    : 19.异步迭代器.py
# @Software: PyCharm


import asyncio


# 自定义异步迭代器
class Reader:
    def __init__(self):
        self.count = 0

    async def readline(self):
        # await asyncio.sleep(1)
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self.readline()
        if val is None:
            raise StopAsyncIteration
        return val

# 错误的
# async for item in Reader():
#     print(item)


async def func():
    obj = Reader()
    # 异步for循环必须在协程函数内执行，协程函数名称随意取名
    async for item in obj:
        print(item)


asyncio.run(func())
