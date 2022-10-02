# -*- coding: utf-8 -*-
# @Time    : 2022/8/26 10:12 下午
# @Author  : 顾安
# @File    : 1. 线程执行顺序.py
# @Software: PyCharm

"""
1. start()
    运行你在target指定的任务函数

2. 为什么target指定之后就可以运行你指定的函数？
    在线程中有内置方法：run()
    run方法就可以运行你当前的指定的任务

3. 既然你直接运行run, 那么为什么要有start()
    为了解耦
        因为在构建线程类的时候我们可以对run()方法进行重写
            在重写的过程中只要关注你当前的任务代码编写就可以
            无需关注你的任务的启动方式。


4. 现在我们知道调用start()会自动运行run() 那么是什么方式运行的run()
    看源码
    start -> _bootstrap[函数引用] -> _bootstrap_inner() -> self.run() 这个self 代表的是Thread类实例对象本身
"""


import threading


class MyThead(threading.Thread):
    def work(self):
        print(1)

    def run(self):
        self.work()
