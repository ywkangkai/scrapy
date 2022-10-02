# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 8:23 下午
# @Author  : 顾安
# @File    : 6. delete_info.py
# @Software: PyCharm

import pymysql


def delete_info():
    db = pymysql.connect(host='localhost', user='root', password='root', db='test')
    cursor = db.cursor()

    sql = "delete from employee where age > %d" % 22
    try:
        cursor.execute(sql)
        db.commit()
        print('数据删除成功...')
    except Exception as e:
        print('数据删除失败:', e)
        db.rollback()
    finally:
        db.close()


if __name__ == '__main__':
    delete_info()


'''
pymysql 偏向于底层

    增删改查操作的时候还需要基于sql语言
    如果大家不会sql语法的话那么是没有办法使用pymysql这个包的
    
有一部分人对于sql是不会的
    如何不通过sql去完成增删改查的任务
    
    orm框架完成增删改查任务
    
    框架特点是通过python中的面向对象的机制去对mysql进行操作
    
    sqlalchemy
'''