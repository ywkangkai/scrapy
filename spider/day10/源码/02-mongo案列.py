#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   02-mongo案列.py    
# Author :   柏汌  

# 要求：获取到爱奇艺视频电视剧数据信息
#
# 网址：https://list.iqiyi.com/www/2/15-------------11-1-1-iqiyi--.html?s_source=PCW_SC
import time

import pymongo
import requests


class Aqiyi(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        self.collection = self.client['spider']['aqy']
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }
        self.url = 'https://pcw-api.iqiyi.com/search/recommend/list'


    def get_data(self, params):
        response = requests.get(self.url, headers=self.headers, params=params)
        # print(response.text)
        return response.json()

    def paras_data(self, data):
        videos = data['data']['list']
        for video in videos:
            # print(video)
            item = {}
            item['name'] = video['name']
            item['playUrl'] = video['playUrl']
            item['description'] = video['description']
            print(item)
            self.save_data(item)

    def save_data(self, item):
        print()
        self.collection.insert_one(item)

    def run(self):
        for i in range(1, 5):
            params = {
                'channel_id':'2',
                'data_type':'1',
                'mode':'11',
                'page_id': i,
                'ret_num':'48',
                'session': '5a5d98bfd7fe740bc527f18d0a71db54',
                'three_category_id':'15;must',
            }
            data = self.get_data(params)
            self.paras_data(data)

if __name__ == '__main__':
    t1 = time.time()
    yk = Aqiyi()
    yk.run()
    print("total cost:", time.time() - t1)

