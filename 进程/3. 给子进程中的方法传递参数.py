# -*- coding: utf-8 -*-
# @Time    : 2022/8/26 8:40 下午
# @Author  : 顾安
# @File    : 3. 给子进程中的方法传递参数.py
# @Software: PyCharm


import os
import time
from multiprocessing import Process


def run_process(name, age, **kwargs):
    for i in range(10):
        print(f'子进程运行中, name={name}, age={age}, pid={os.getpid()}')
        print(kwargs)
        time.sleep(0.2)


if __name__ == '__main__':
    p = Process(target=run_process, args=('顾安', 18), kwargs={'address': '长沙'})
    p.start()
    print(p.is_alive())
    # 系统回收进程需要时间

    """
    如果大家对僵尸进程感兴趣
        务必在沙箱环境中测试
    """
    p.terminate()
    p.join()
    print(p.is_alive())


