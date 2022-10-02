# -*- coding: utf-8 -*-
# @Time    : 2022/9/7 10:14 下午
# @Author  : 顾安
# @File    : 6. 使用redis包获取key.py
# @Software: PyCharm


from redis import *

if __name__ == "__main__":
    try:
        # 创建Redis对象，与redis服务器建⽴连接
        sr = Redis(db=0)
        # 获取所有的键
        result = sr.keys()
        # 输出响应结果，所有的键构成⼀个列表，如果没有键则返回空列表
        print(result)
    except Exception as e:
        print(e)
