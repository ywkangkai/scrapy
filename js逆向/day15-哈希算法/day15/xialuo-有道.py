# encoding: utf-8

import hashlib
import requests,time,random
import math


class Crawl():

    def __init__(self):
        self.headers = {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=322076570@10.169.0.83; JSESSIONID=aaaZhLm5ZNK87a08TerIx; OUTFOX_SEARCH_USER_ID_NCOO=1158799533.2810698; ___rl__test__cookies={}'.format(math.ceil(time.time() * 1000)),

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',

            'Referer': 'http://fanyi.youdao.com/',
        }

        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    def spider(self,key):

        times = str(math.ceil(time.time() * 1000) + random.randint(1, 10))
        sign = self.Md5("fanyideskweb" + key + str(times) + "Tbh5E8=q6U3EXe+&L[4c@")

        data = {
            "i": key,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": times,
            "sign": sign,
            "lts": times[:-1],
            "bv": "cda1e53e0c0eb8dd4002cefc117fa588",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME"
        }
        res = requests.post(self.url, data=data, headers=self.headers).json()
        if res.get('errorCode') == 0:
            print('执行的结果:' + res.get('translateResult')[0][0]['tgt'])

    def Md5(self,value):
        md = hashlib.md5()
        md.update(value.encode('utf8')) # 接收字节类型  16进制表示
        return md.hexdigest()

if __name__ == '__main__':
    while True:
        s = input('请输入你不懂的话术&&输入y退出:')
        Crawl().spider(s)
        if s == 'y':
            break

