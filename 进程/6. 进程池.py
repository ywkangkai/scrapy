# -*- coding: utf-8 -*-
# @Time    : 2022/8/26 9:45 下午
# @Author  : 顾安
# @File    : 6. 进程池.py
# @Software: PyCharm


import os, time, random
from multiprocessing import Pool


def worker(msg):
    # 记录当前程序开始执行的时间
    p_start = time.time()
    print(f'{msg}开始执行, 进程号为: {os.getpid()}')
    time.sleep(random.random() * 2)
    p_stop = time.time()
    print(msg, f'执行完毕, 耗时: {p_stop - p_start}')


if __name__ == '__main__':
    main_start = time.time()
    po = Pool(3)
    for i in range(10):
        # 如何在进程池中运行代码
        # 异步执行 apply_async
        po.apply_async(worker, (i,))
        # 同步执行
        # po.apply(worker, (i,))

    po.close()
    # 等待进程池中的执行完毕之后主进程解堵塞
    # join必须要在关闭进程池之后使用
    po.join()
    main_stop = time.time()
    print('程序耗时:', main_stop - main_start)


