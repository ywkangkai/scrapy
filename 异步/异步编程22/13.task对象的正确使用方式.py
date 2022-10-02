# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 8:53 下午
# @Author  : 顾安
# @File    : 13.task对象的正确使用方式.py
# @Software: PyCharm


import asyncio


async def func_1():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '这是一个返回值'


async def func_2():
    print(3)
    await asyncio.sleep(2)
    print(4)
    return '这是一个返回值'


task_list = [
    func_1(),
    func_2()
]

# 如果在列表中创建task对象 那么必须在创建task对象之前事件循环先要被创建
asyncio.run(asyncio.wait(task_list))


'''
如果在列表中放入了协程对象之后交给事件循环去运行时，
会自动为每一个协程对象创建一个task对象

执行顺序是随机的
    因为func1放入到事件循环中会立即执行么？
        先创建task对象

为什么要手动创建:
    为了提升性能，当事件循环拿到task对象之后直接并发执行了
    
如何在列表中使用create_task
    保证当前这个列表不能被执行
    
    async def main():
        task_list = [
            asyncio.create_task(func1()),
            asyncio.create_task(func2()),
        ]

main()
    -> 只是一个对象
    
'''

asyncio.ensure_future()



