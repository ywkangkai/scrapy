#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   04-多线程案列mongo数据.py    
# Author :   柏汌  


import threading
import requests
# import pymongo
import time
from queue import Queue



class Aqiyi:
    def __init__(self):
        # self.client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        # self.collection = self.client['spider']['aqy1']
        self.url = 'https://pcw-api.iqiyi.com/search/recommend/list?channel_id=2&data_type=1&mode=11&page_id={}&ret_num=48&session=734d98ec51d15a8f5356cb4a5f78433b&three_category_id=15;must'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }
        self.url_queue = Queue()
        self.json_queue = Queue()
        self.content_list_queue = Queue()


    def get_url(self):
        # time.sleep(5)
        for i in range(1, 5):
            self.url_queue.put(self.url.format(i))

    def get_data(self):
        while True:
            print('得到数据')
            # q队列get会取出数据  但是计数不会减一
            url = self.url_queue.get()
            response = requests.get(url, headers=self.headers)
            # print(response.json())
            self.json_queue.put(response.json())
            print(self.url_queue.qsize())
            self.url_queue.task_done()

    def parse_data(self):
        while True:
            print('解析数据')
            data = self.json_queue.get()
            for video in data['data']['list']:
                item = {}
                item['name'] = video['name']
                item['playUrl'] = video['playUrl']
                item['description'] = video['description']
                self.content_list_queue.put(item)
            self.json_queue.task_done()



    # def save_data(self):
    #     while True:
    #         item = self.content_list_queue.get()
    #         print(item)
    #         self.collection.insert_one(item)
    #         self.content_list_queue.task_done()


    def main(self):
        # 存放所以线程
        thread_list = []
        # 创建子线程执行get_url
        t_url = threading.Thread(target=self.get_url)
        thread_list.append(t_url)
        # 开启发送请求线程
        for i in range(3):
            t_pares = threading.Thread(target=self.get_data)
            thread_list.append(t_pares)
        # 提取数据
        t_content = threading.Thread(target=self.parse_data)
        thread_list.append(t_content)
        # 保存数据
        # t_save = threading.Thread(target=self.save_data)
        # thread_list.append(t_save)
        # 启动线程
        for t in thread_list:
            # 把子线程设置成守护主线程，主线程级别最高，主线程结束，子线程也结束
            t.setDaemon(True)
            # 启动线程
            t.start()
            t.join() #join所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程在终止，例子见下面三

        for i in [self.url_queue, self.json_queue, self.content_list_queue]:
            i.join()  # 让主线程阻塞  等待队列计数为0



if __name__ == '__main__':
    t1 = time.time()
    yk = Aqiyi()
    yk.main()
    print("total cost:", time.time() - t1)







