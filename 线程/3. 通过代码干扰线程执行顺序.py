# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 8:55 下午
# @Author  : 顾安
# @File    : 3. 通过代码干扰线程执行顺序.py
# @Software: PyCharm

import time
import threading


def test1():
    for i in range(5):
        print('test1')


def test2():
    for i in range(5):
        print('test2')


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    t1.join()  # 当线程1执行完毕之后才会去执行线程2
    t2.start()
    time.sleep(1)


if __name__ == '__main__':
    main()


'''
如果你在写爬虫的时候发现数据乱了
    让线程等待另外一个线程执行完毕之后再去执行
    
在线程中可能会出现一种情况
    线程2执行需要线程1的执行结果
    
    线程之间的切换是随机的
    
    如果线程1任务没有执行完毕就立即执行线程2 
        可以会造成代码崩溃
    
    可以使用join方法来干扰线程之间的切换
    
    
下载为例：
    线程1 获取数据 join()
    线程2 下载数据
    
因为如果现在有十部电影需要去下载
    生成十个线程去获取十部电影的数据   http websocket
    
    生成十个线程去下载十部电影的数据   with open
'''
