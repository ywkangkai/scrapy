# -*- coding: utf-8 -*-
# @Time    : 2022/8/26 10:01 下午
# @Author  : 顾安
# @File    : 7. 如何在进程池中使用队列.py
# @Software: PyCharm


import os, time
from multiprocessing import Manager, Pool


# 写数据
def writer(q):
    print(f'写入进程启动, 进程为: {os.getpid()}')
    for i in 'abcdefg':
        q.put(i)


def reader(q):
    print(f'读取进程启动, 进程为: {os.getpid()}')
    for i in range(q.qsize()):
        print(f'获取到的元素为: {q.get()}')


if __name__ == '__main__':
    q = Manager().Queue()
    po = Pool()
    po.apply_async(writer, (q,))
    time.sleep(2)
    po.apply_async(reader, (q,))
    po.close()
    po.join()
