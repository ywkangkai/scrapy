# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 9:58 下午
# @Author  : 顾安
# @File    : 20. 异步上下文管理器.py
# @Software: PyCharm

"""
想要异步的进行文件操作但是不想手动的去关闭文件流
想要异步的去进行数据库操作但是不想手动的去关闭游标对象和连接对象
想要异步的去执行TCP代码但是不想手动的进行资源释放
"""

import asyncio


class AsyncContextManager:
    def __init__(self, conn=None):
        self.conn = conn

    async def do_something(self):
        # 异步操作数据库
        print('这个是操作数据库的代码')
        return 'crud'

    async def __aenter__(self):
        # 异步连接数据库
        print('当前数据库连接代码被执行了')
        self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # 异步关闭数据库连接
        print('当前退出数据库代码被执行了')
        await asyncio.sleep(1)


async def func():
    # 上下文管理器处理也需要在协程函数中运行
    async with AsyncContextManager() as f:
        result = await f.do_something()
        print(result)


asyncio.run(func())
