#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   01-复习mongo.py    
# Author :   柏汌  

import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
collection = client['students']['stu']

# 插入单条数据
student = {'id': '20170101', 'name': 'Jordan', 'age': 20, 'gender': 'male' }
reslut = collection.insert_one(student)
print(reslut)


# 插入多条数据
student1 = { 'id': '20170101', 'name': 'Jordan', 'age': 20, 'gender': 'male' }
student2 = { 'id': '20170202', 'name': 'Mike', 'age': 21, 'gender': 'male' }
collection.insert_many([student1, student2])
