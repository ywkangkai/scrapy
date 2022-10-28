#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   03-多进程使用方法.py    
# Author :   柏汌  

import requests
import pymongo
import time
from multiprocessing import Process
from multiprocessing import JoinableQueue as Queue

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
collection = client['spider']['aqy2']

class Aqiyi(object):
    def __init__(self):

        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }
        self.url = 'https://pcw-api.iqiyi.com/search/recommend/list?channel_id=2&data_type=1&mode=11&page_id={}&ret_num=48&session=6c2d98a539ad1a4cd5c15b0ed541886b&three_category_id=15;must'
        self.url_queue = Queue()
        self.json_queue = Queue()
        self.content_queue = Queue()

    def get_url(self):
        print(11111111111)
        for i in range(1, 10):
            self.url_queue.put(self.url.format(i))


    def get_data(self):
        while True:
            url = self.url_queue.get()

            response = requests.get(url, headers=self.headers)
            # print(response.text)
            # return response.json()
            self.json_queue.put(response.json())
            self.url_queue.task_done()


    def paras_data(self):
        while True:
            data = self.json_queue.get()
            videos = data['data']['list']
            for video in videos:
                # print(video)
                item = {}
                item['name'] = video['name']
                item['playUrl'] = video['playUrl']
                item['description'] = video['description']
                print(item)
                self.content_queue.put(item)
                # self.save_data(item)
            self.json_queue.task_done()


    def save_data(self):
        while True:
            item = self.content_queue.get()
            collection.insert_one(item)
            self.content_queue.task_done()

    def run(self):

        process_list = []

        # 获取所有的网址
        t_url = Process(target=self.get_url)
        process_list.append(t_url)

        # 发送请求
        for i in range(5):
            t_parse = Process(target=self.get_data)
            process_list.append(t_parse)
        # 提取数据
        t_content = Process(target=self.paras_data)
        process_list.append(t_content)
        for i in range(3):
            t_save = Process(target=self.save_data)
            process_list.append(t_save)
        # print(1111111)
        print(process_list)
        for t in process_list:
            # print(t)
            t.daemon = True
            t.start()
            time.sleep(0.5)


        for q in [self.url_queue, self.json_queue, self.content_queue]:
            q.join()

        print('主线程结束！！！！！！！！！')


if __name__ == '__main__':
    t1 = time.time()
    yk = Aqiyi()
    yk.run()
    print("total cost:", time.time() - t1)








