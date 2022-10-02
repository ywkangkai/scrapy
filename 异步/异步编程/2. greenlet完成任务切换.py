# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 8:28 下午
# @Author  : 顾安
# @File    : 2. greenlet完成任务切换.py
# @Software: PyCharm


from greenlet import greenlet


def func1():
    print(1)
    # 当前代码可以完成关于任务的切换
    gr2.switch()
    print(2)
    gr2.switch()


def func2():
    print(3)
    gr1.switch()
    print(4)
    gr1.switch()


gr1 = greenlet(func1)
gr2 = greenlet(func2)

# 启动你指定的任务
gr1.switch()
