# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 9:06 下午
# @Author  : 顾安
# @File    : 1. 连接数据库.py
# @Software: PyCharm

import sqlalchemy

HOST = 'localhost'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'
DB = 'test'

# 数据库路由
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}"


# 1. 创建数据库引擎
engine = sqlalchemy.create_engine(DB_URI)

# 2. 通过引擎连接数据库
conn = engine.connect()

# 3. 通过conn对象执行sql语句
result = conn.execute('select now()')

# 4. 执行完成后打印返回的数据
print(result.fetchone())

# 5. 关闭连接
conn.close()



