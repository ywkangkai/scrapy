#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   04-csv案例.py    
# Author :   柏汌  

# 采集B站上视频数据信息
#
# 	网址：https://search.bilibili.com/video?keyword=%E7%BE%8E%E5%A5%B3&from_source=webtop_search&spm_id_from=333.1007&search_source=5

import requests
import csv

with open('b站.csv', 'a', encoding='utf-8', newline='')as f:
    finame = ['作者', '详情地址', '标题']
    csv_data = csv.DictWriter(f, fieldnames=finame)
    csv_data.writeheader()

    for i in range(3, 10):
        url = 'https://api.bilibili.com/x/web-interface/search/type?__refresh__=true&_extra=&context=&page={}&page_size=42&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=%E7%BE%8E%E5%A5%B3&qv_id=05oL95VN5GsPwEx5fuf1QI9vg6cvOg7l&category_id=&search_type=video&dynamic_offset=30&preload=true&com2co=true'.format(i)
        headers = {
            'cookie': "buvid3=512EA149-F880-22BB-EB87-F4C8578999D267425infoc; _uuid=87259181-910CF-124E-1B37-F2101ED2F524369004infoc; buvid4=26FDBE32-69F5-F891-EE76-68BB0E8AB3B668394-022031013-AiqhsCVq4shONtxebl+wxw%3D%3D; rpdid=|(umuum)YRJR0J'uYRY))mm~|; i-wanna-go-back=-1; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; blackside_state=0; nostalgia_conf=-1; LIVE_BUVID=AUTO1916483040807628; CURRENT_QUALITY=80; b_ut=5; fingerprint=c3224de012671f54d78c51956cb06be2; DedeUserID=1892223867; DedeUserID__ckMd5=4e3cb95f66216458; buvid_fp=c3224de012671f54d78c51956cb06be2; hit-dyn-v2=1; PVID=1; b_nut=100; bp_video_offset_1892223867=717488116780236900; SESSDATA=3d35e59f%2C1681713767%2C0f22e%2Aa1; bili_jct=1e76362b152c51b884185c3a582aaf14; CURRENT_FNVAL=16; sid=7t6gvw0i; b_lsid=BA1FBE31_183F056FF6A",
            # 'referer': 'https://www.bilibili.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        # print(response.text)


        for res in response.json()['data']['result']:
            # print(res)
            item = {}
            item['作者'] = res['author']
            item['详情地址'] = res['arcurl']
            item['标题'] = res['tag']
            csv_data.writerow(item)
            print(item)
