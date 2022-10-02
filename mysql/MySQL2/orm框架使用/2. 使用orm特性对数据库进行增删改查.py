# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 9:19 下午
# @Author  : 顾安
# @File    : 2. 使用orm特性对数据库进行增删改查.py
# @Software: PyCharm


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

"""
declarative_base: sql orm的基类 创建orm的类必须要继承当前这个基类
create_engine: 创建数据库引擎
Column: 对当前表中的字段进行映射
Integer, String: 对应数据库中的字段类型
sessionmaker: 会话保持 保证当前的连接的有效性
"""

HOST = 'localhost'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'
DB = 'test'

DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}"

engine = create_engine(DB_URI)
# 构建orm基类
Base = declarative_base(engine)
# 构建会话
session = sessionmaker(engine)()


# 通过类去创建一张表
class UserInfo(Base):
    # 表名
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(10))
    age = Column(Integer)
    address = Column(String(10))


# 如果当前数据库中已经存在同名的表 那么不会重复创建
# 如果当前的表名称一致, 但是表结构不一样则报错
Base.metadata.create_all()


# 新增数据
info = UserInfo(username='柏汌老师', age=20, address='长沙')
# 将类属性中的值映射到数据表中
# session.add(info)
# 确认提交x
# session.commit()

# 新增多条数据
# session.add_all([
#     UserInfo(username='夏洛老师', age=18, address='长沙'),
#     UserInfo(username='木木老师', age=16, address='南京'),
#     UserInfo(username='安娜老师', age=18, address='北京')
# ])
#
# session.commit()


# 查询
# 查询所有数据
info_list = session.query(UserInfo).all()
for item in info_list:
    print(item.id, item.username, item.age, item.address)

print('-' * 20)

# 查询指定列
name_list = session.query(UserInfo.username, UserInfo.age).all()
print(name_list)
for name in name_list:
    print('name:', name[0], 'age:', name[1])

print('-' * 20)

# 获取返回数据的第一行
item = session.query(UserInfo.username).first()
print(item[0])

print('-' * 20)


# 使用filter()方法进行条件筛选过滤
item_list = session.query(UserInfo.username, UserInfo.age).filter(UserInfo.age >= 18).all()
for item in item_list:
    print(item[0], item[1])

print('-' * 20)

# 排序
item_list = session.query(UserInfo.id, UserInfo.username, UserInfo.age).order_by(UserInfo.id.desc()).all()
print(item_list)

print('-' * 20)

# 多条件查询
item_list = session.query(UserInfo.username, UserInfo.age, UserInfo.address).filter(
    UserInfo.age >= 18, UserInfo.address == '长沙'
).all()

print(item_list)

# 或查询
from sqlalchemy import or_
item_list = session.query(UserInfo.username, UserInfo.age, UserInfo.address).filter(
    or_(UserInfo.age >= 18, UserInfo.address == '长沙')
).all()

print(item_list)

print('-' * 20)

# 比较查询 模糊查询以及范围查询(非连续)
item_list = session.query(UserInfo.username, UserInfo.age, UserInfo.address).filter(
    UserInfo.age == 18
).all()

print(item_list)

"""
需要大家根据搜索引擎学会 sqlalchemy 的连续范围查询
"""

print('-' * 20)

# 取反查询
item_list = session.query(UserInfo.username, UserInfo.age, UserInfo.address).filter(
    UserInfo.age != 18
).all()
print(item_list)

print('-' * 20)

# 模糊查询
item_list = session.query(UserInfo.username).filter(
    UserInfo.username.like('安%')
).all()
print(item_list)

print('-' * 20)

# in 非连续
# in_和or_不一样 or_需要手动导入 in_不需要
item_list = session.query(UserInfo.username, UserInfo.age).filter(
    UserInfo.age.in_([16, 20])
).all()
print(item_list)

print('-' * 20)

# 聚合函数
count = session.query(UserInfo).count()
print(count)

print('-' * 20)

# 切片查询
item_list = session.query(UserInfo.username).all()[:3]
print(item_list)

print('-' * 20)
# 数据修改
# 修改柏汌老师的年龄
session.query(UserInfo).filter(UserInfo.username == '柏汌老师').update({'age': 22})
session.commit()

item_list = session.query(UserInfo.username, UserInfo.age).filter(UserInfo.username == '柏汌老师').all()
print(item_list)

print('-' * 20)

# 数据删除
# 删除名称为木木老师的数据
session.query(UserInfo).filter(UserInfo.username == '木木老师').delete()
session.commit()

item_list = session.query(UserInfo).all()
# 现在大家将打印代码写出来
for item in item_list:
    print(item.username, item.age, item.address)
















