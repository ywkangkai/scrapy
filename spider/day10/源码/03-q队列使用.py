#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   03-q队列使用.py    
# Author :   柏汌  


from queue import Queue
q = Queue(maxsize=5)
item = {}
# for i in range(6):
q.put(item)   # 放入数据到队列里面  队列满的时候会等待
q.put_nowait(item) # 不等待直接放， 不等待直接存放数据   队列满则报错
q.get()  # 取出数据 队列为空则等待
q.task_done()
print(q.qsize())
# q.get()  # 取出数据 队列为空则等待
# q.task_done()
# q.get_nowait()  # 不等待直接取值   没有数据报错
# print(q.qsize())
q.join()  # 队列计数使用

# put使用时  计数会+1  get不会-1   get和task_done一起使用才会-1










