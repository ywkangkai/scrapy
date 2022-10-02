# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 8:36 下午
# @Author  : 顾安
# @File    : 7. 测试数据的创建.py
# @Software: PyCharm


import pymysql


def main():
    db = pymysql.connect(host='localhost', user='root', password='root', db='test')
    cursor = db.cursor()

    try:
        for item in range(100000):
            cursor.execute("insert into test_index values('t_%d')" % item)
        db.commit()
        print('数据插入成功...')
    except Exception as e:
        print('数据插入失败: ', e)
        db.rollback()
    finally:
        db.close()


if __name__ == '__main__':
    main()


'''
什么是框架:
    想要打电话
        必须要有一个手机
        在手机内部是不是已经具备了打电话的功能
        
        手机能不能自己打电话？
        需要通过用户自己手动控制, 去调用打电话的功能
        
    框架本身已经具备了一些功能
        这些功能是需要开发者自己手动调用才可以完成一些任务
        
完成一个爬虫功能
    只是需要大家去安装一些爬虫框架就可以简单的实现一些爬虫功能
    
网站开发
    网站开发框架
    
orm 定义
    mysql存储数据的方式 ---> 表去存储
        表最重要的一个组成部分是字段
    
    想要通过python语言去控制mysql的话
        必须使用python语言去构建表结构
        
        学生表
     |----|----|----|----|-
        id name  age  address
     |----|----|----|----|-
        1   abc  18      长沙


    类
        class Student:
            id = 1
            name = abc
            age = 18
            address = 长沙
'''