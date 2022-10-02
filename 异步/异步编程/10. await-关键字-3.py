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
    # 注意：在当前代码中使用await进行io等待后, 会堵塞代码。当response_1执行完毕后解堵塞继续往下执行
    response_1 = await others()
    print(response_1)

    # response_2同理, 等待others任务执行完毕后才能继续往下执行
    response_2 = await others()
    print(response_2)


asyncio.run(func())


'''
迭代器
生成器 -> 协程基础
装饰器 -> fastapi、flask
'''