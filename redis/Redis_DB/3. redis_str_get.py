# -*- coding: utf-8 -*-
# @Time    : 2022/9/7 10:08 下午
# @Author  : 顾安
# @File    : 3. redis_str_get.py
# @Software: PyCharm


from redis import *

if __name__ == "__main__":
    try:
        # 创建Redis对象，与redis服务器建⽴连接
        sr = Redis(db=1)
        # 获取键name的值
        result = sr.get('name')
        # 输出键的值，如果键不存在则返回None
        print(result.decode('utf-8'))
    except Exception as e:
        print(e)
