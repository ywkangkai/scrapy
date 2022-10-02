# -*- coding: utf-8 -*-
# @Time    : 2022/8/26 8:20 下午
# @Author  : 顾安
# @File    : 1. 进程的创建.py
# @Software: PyCharm


import time
from multiprocessing import Process


def run_process():
    while True:
        print('当前任务被子进程运行...')
        time.sleep(1)


if __name__ == '__main__':
    # 1. 创建一个进程对象
    p = Process(target=run_process)
    # 2. 启动进程
    p.start()

    while True:
        print('当前任务被主进程运行...')
        time.sleep(1)



