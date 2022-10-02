# -*- coding: utf-8 -*-
# @Time    : 2022/9/7 10:12 下午
# @Author  : 顾安
# @File    : 5. redis_str_delete.py
# @Software: PyCharm


from redis import *

if __name__ == "__main__":
    try:
        # 创建Redis对象，与redis服务器建⽴连接
        sr = Redis(db=1)
        # 设置键name的值，如果键已经存在则进⾏修改，如果键不存在则进⾏添加
        result = sr.delete('name')
        # 输出响应结果，如果删除成功则返回受影响的键数，否则则返回0
        print(result)
    except Exception as e:
        print(e)
