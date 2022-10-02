# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 9:38 下午
# @Author  : 顾安
# @File    : 上下文管理器.py
# @Software: PyCharm



'''
在python中的上下文管理器是基于当前用户在运行程序中状态进行自动操作

基于asyncio的协程上下文管理器
'''


class A:
    def __init__(self):
        self.a = 0

    def __enter__(self):
        # 在当前魔术方法中 如果使用的是with关键字 则自动运行当前方法
        # 连接mysql的代码
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 如果在上下文管理器中运行到最后一段代码结束时 运行当前方法
        # 关闭mysql游标的方法
        return None

    async def __aenter__(self):
        return self

    def __aexit__(self, exc_type, exc_val, exc_tb):
        pass