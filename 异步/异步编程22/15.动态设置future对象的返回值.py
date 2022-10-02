# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 9:16 下午
# @Author  : 顾安
# @File    : 15.动态设置future对象的返回值.py
# @Software: PyCharm


import asyncio


async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result('这是一个测试结果')


async def main():
    # 获取事件循环
    loop = asyncio.get_running_loop()

    # 创建一个任务, 并且当前任务没有绑定任何行为, 则这个任务永远不知道什么时候结束
    fut = loop.create_future()

    # 手动设置future任务的最终结果
    await loop.create_task(set_after(fut))

    # 等待Future对象获取最终的结果, 否则就一直等
    data = await fut
    print(data)


asyncio.run(main())


'''
当前的future对象可以通过set_result去设置一个返回值

task对象是继承了future对象 在task对象执行完协程函数之后 会自动调用set_result方法将协程函数中的返回值设置到
接收对象当中
'''