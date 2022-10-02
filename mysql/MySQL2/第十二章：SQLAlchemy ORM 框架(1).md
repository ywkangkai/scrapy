## 第十二章：SQLAlchemy - ORM 框架

SQLAlchemy是用Python编程语言开发的一个开源项目。它提供了SQL工具包和ORM（对象关系映射）工具，使用MIT许可证发行。

SQLAlchemy最初在2006年2月发行，发行后便很快的成为Python社区中最广泛使用的ORM工具之一，丝毫不亚于Django自带的ORM框架。

SQLAlchemy采用简单的Python语言，提供高效和高性能的数据库访问，实现了完整的企业级持久模型。它的理念是，SQL数据库的量级和性能比对象集合重要，而对象集合的抽象又重要于表和行。



### 安装sqlalchemy

```python
pip3 install sqlalchemy
pip3 install pymysql
```

使用MySQL作为数据库，使用pymysql作为驱动，因此需要安装pymysql



### 数据连接

在连接数据库前，需要使用到一些配置信息，然后把它们组合成满足以下条件的字符串：

```python
dialect+driver://username:password@host:port/database
```

- dialect：数据库，如：sqlite、mysql、oracle等
- driver：数据库驱动，用于连接数据库的，本文使用pymysql
- username：用户名
- password：密码
- host：IP地址
- port：端口
- database：数据库

```python
HOST = 'localhost'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'
DB = 'test'

# dialect + driver://username:passwor@host:port/database
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'
```

建议将配置信息放到你的配置文件中，如config.py



### 创建引擎并连接数据库

```python
HOST = 'localhost'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'
DB = 'test'

DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}"

engine = create_engine(DB_URI)
conn = engine.connect()  # 连接
result = conn.execute('SELECT 1')  # 执行SQL
print(result.fetchone())  
conn.close()  # 关闭连接
```



### 创建orm模型并映射到数据库中

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

HOST = 'localhost'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'
DB = 'test'

DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}"

engine = create_engine(DB_URI)
Base = declarative_base(engine)  # SQLORM基类
session = sessionmaker(engine)()  # 构建session对象


class UserInfo(Base):
    __tablename__ = 'user_info'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(10))
    age = Column(Integer, default=0)
    address = Column(String(10))


Base.metadata.create_all()
```

执行上面代码，将会在数据库中生成对应的映射表user_info。



### 新增数据

```python
info = UserInfo(username='柏汌', age=18, address='长沙')
session.add(info)
session.commit()
```

数据的批量添加：

```python
session.add_all([
    UserInfo(username='夏洛', age=20, address='南京'),
    UserInfo(username='木木', age=16, address='上海')
])

session.commit()
```



### 查询数据

##### 获取所有数据

```python
info_list = session.query(UserInfo).all()

# 查询所有
for item in info_list:
    print(item.username, item.password, item.address)
```

查询得到的 info_list 是一个包含多个 UserInfo 对象的列表



##### 指定查询列

```python
item_list = session.query(UserInfo.username).all()
print(item_list)
```



##### 获取返回数据的第一行

```python
item = session.query(UserInfo.username).first()
print(item)  
```



##### 使用filter()方法进行筛选过滤

```python
item_list = session.query(UserInfo.username).filter(UserInfo.age >= 18).all()
print(item_list)
```



##### 使用order_by()进行排序

```python
item_list = session.query(UserInfo.username, UserInfo.age).order_by(UserInfo.age.desc()).all() # desc()表示倒序
print(item_list)
```



##### 多个查询条件 (and和or)

```python
# 默认为and, 在filter()中用,分隔多个条件表示and
item_list = session.query(UserInfo.username, UserInfo.age, UserInfo.address).filter(
    UserInfo.age >= 10, UserInfo.address == '长沙'
).all()
print(item_list)


# 使用or_连接多个条件
from sqlalchemy import or_

item_list = session.query(UserInfo.username, UserInfo.age, UserInfo.address).filter(
    or_(UserInfo.age >= 18, UserInfo.address == '长沙')
).all()
print(item_list)
```



##### equal、like、in

```python
# 等于
item_list = session.query(UserInfo.username, UserInfo.age, UserInfo.address).filter(
    UserInfo.age == 18
).all()
print(item_list)

# 不等于
item_list = session.query(UserInfo.username, UserInfo.age, UserInfo.address).filter(
    UserInfo.age != 18
).all()
print(item_list)

# like
item_list = session.query(UserInfo.username, UserInfo.age, UserInfo.address).filter(
    UserInfo.username.like('木%')
).all()
print(item_list)

# in
item_list = session.query(UserInfo.username, UserInfo.age, UserInfo.address).filter(
    UserInfo.age.in_([16, 18])
).all()
print(item_list)
```



##### count计算个数

```python
count = session.query(UserInfo).count()
print(count)
```



##### 切片

```python
item_list = session.query(UserInfo.username).all()[:2]
print(item_list)
```



### 修改数据

修改数据可以使用update()方法，update完成后记得执行session.commit()

```python
session.query(UserInfo).filter(UserInfo.username == '柏汌').update({'age': 22})
session.commit()

item = session.query(UserInfo.username, UserInfo.age).filter(UserInfo.username == '柏汌').first()
print(item) 
```



### 删除数据

删除数据使用delete()方法，同样也需要执行session.commit()提交事务

```python
# 删除名称为夏洛的数据
session.query(UserInfo).filter(UserInfo.name == '夏洛').delete()
session.commit()

item_list = session.query(UserInfo.username, UserInfo.age, UserInfo.address).all()
print(item_list)
```

