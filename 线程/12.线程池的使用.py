# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 10:25 下午
# @Author  : 顾安
# @File    : 12.线程池的使用.py
# @Software: PyCharm


"""
为什么要去学线程池
    因为手动开启线程比较麻烦
    并且如果线程数量过多会导致系统卡顿
    所以我们可以创建一个指定数量的线程池来创建线程
"""
import threading
from concurrent.futures import ThreadPoolExecutor
import time


# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum


# 创建一个包含2条线程的线程池
pool = ThreadPoolExecutor(max_workers=2)
# 向线程池提交一个task, 50会作为action()函数的参数
future1 = pool.submit(action, 10)
# 向线程池再提交一个task, 100会作为action()函数的参数
future2 = pool.submit(action, 15)
# 判断future1代表的任务是否结束
print(future1.done())
time.sleep(3)
# 判断future2代表的任务是否结束
print(future2.done())
# 查看future1代表的任务返回的结果
print(future1.result())
# 查看future2代表的任务返回的结果
print(future2.result())
# 关闭线程池
pool.shutdown()
