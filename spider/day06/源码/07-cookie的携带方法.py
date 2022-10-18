#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   07-cookie的携带方法.py    
# Author :   柏汌  

# 第一种在headers里面携带cookie

# import requests
# url = 'http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice'
# headers = {
#     'Cookie': 'JSESSIONID=A06FCFADA1AEB4AEF1CB884840508AC0; routeId=.uc1; _sp_ses.2141=*; insert_cookie=45380249; _sp_id.2141=417fc66b-30c0-460a-a617-d7429be1a15b.1663329841.3.1665579540.1665563955.3ff2ed03-4d31-4bbe-8729-f5da0af1c561',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
# }
#
# requests.get(url, headers=headers)


# 第二种当做参数传递
# import requests
# url = 'http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
# }
# cookies = {'JSESSIONID': '204BABEA1EEB56A40A98F189227102C', 'insert_cookie': '45380249', 'routeId': '.uc1',
#           '_sp_ses.2141': '*',
#           '_sp_id.2141': '4d159bf3-398b-4dd5-8e07-78ee07cbcbf9.1662302323.3.1662383561.1662359150.afa633dd-c1a8-4d81-90a7-01b0c3630055'
#            }
#
# response = requests.get(url, headers=headers, cookies=cookies)
# # 查看cookie信息
# print(response.request.headers)



# 使用session处理cookie
# import requests
#
# session = requests.session()
# session.get(url, headers)

import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
url1 = 'http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice'
url2 = 'http://www.cninfo.com.cn/new/data/szse_stock.json'
session = requests.session()
response = session.get(url1, headers=headers)
# 观察第一次请求返回的cookie
print(response.cookies)
res = session.get(url2, headers=headers)
# 观察第二次请求携带的cookie
print(res.request.headers)
