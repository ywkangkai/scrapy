# -*- coding: utf-8 -*-
# @Time    : 2022/8/26 9:22 下午
# @Author  : 顾安
# @File    : 5. 进程中的队列.py
# @Software: PyCharm

"""
什么是队列:
    数据结构
    想象成一个列表
    先进来的数据，在获取的时候会从队列中剔除
"""


import time, random
from multiprocessing import Process, Queue


# 写数据
def write(q):
    for value in ['a', 'b', 'c']:
        q.put(value)
        time.sleep(random.random())


def read(q):
    while True:
        if not q.empty():
            value = q.get()
            print('子进程_2 获取到的元素为: ', value)
        else:
            break


if __name__ == '__main__':
    # 如果没有定义队列的最大长度 那么会根据你当前机器的内存自行调整
    q = Queue()
    p_write = Process(target=write, args=(q,))
    p_read = Process(target=read, args=(q,))

    p_write.start()
    p_write.join()
    p_read.start()
    p_read.join()
    print('数据读取完毕...')
