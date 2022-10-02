# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 9:29 下午
# @Author  : 顾安
# @File    : 16.threading_precess_future.py
# @Software: PyCharm


import time
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor


def func(value):
    time.sleep(1)
    print(value)


# 创建线程池
pool = ThreadPoolExecutor(max_workers=5)

# 创建进程池
# pool = ProcessPoolExecutor(max_workers=5)

for i in range(10):
    # 当前最线程数为5个 在执行十个任务时 后五个任务会等待
    # 直到有一个任务执行完毕之后则进行任务的添加
    fut = pool.submit(func, i)
    print(fut)
