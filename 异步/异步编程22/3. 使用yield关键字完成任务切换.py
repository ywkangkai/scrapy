# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 8:36 下午
# @Author  : 顾安
# @File    : 3. 使用yield关键字完成任务切换.py
# @Software: PyCharm


def func1():
    yield 1
    yield from func2()  # 暂停
    yield 2


def func2():
    yield 3
    yield 4


f1 = func1()
for item in f1:
    print(item)


'''
当前任务可以牵强的称之为多任务切换
    从上往下切换
    
'''