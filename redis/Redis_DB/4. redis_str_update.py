# -*- coding: utf-8 -*-
# @Time    : 2022/9/7 10:11 下午
# @Author  : 顾安
# @File    : 4. redis_str_update.py
# @Software: PyCharm


from redis import *

if __name__ == "__main__":
    try:
        # 创建Redis对象，与redis服务器建⽴连接
        sr = Redis(db=1)
        # 设置键name的值，如果键已经存在则进⾏修改，如果键不存在则进⾏添加
        result = sr.set('name', '安娜')
        # 输出响应结果，如果操作成功则返回True，否则返回False
        print(result)
        name = sr.get('name')
        print(name.decode())
    except Exception as e:
        print(e)
