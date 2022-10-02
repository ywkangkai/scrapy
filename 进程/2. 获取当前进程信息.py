# -*- coding: utf-8 -*-
# @Time    : 2022/8/26 8:26 下午
# @Author  : 顾安
# @File    : 2. 获取当前进程信息.py
# @Software: PyCharm


"""
获取创建的进程pid
"""

import os
from multiprocessing import Process


def run_process():
    print('子进程已启动, 当前子进程的pid为: ', os.getpid(), '当前子进程的父进程的pid为: ', os.getppid())
    print('子进程结束...')


if __name__ == '__main__':
    print('主进程的pid为: ', os.getpid(), '当前子进程的父进程的pid为: ', os.getppid())
    p = Process(target=run_process)
    p.start()

"""
当前子进程需要依赖主进程
"""

