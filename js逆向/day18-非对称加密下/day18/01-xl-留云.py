

import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs

class Login():

    def __init__(self):
        self.item1 = None
        self.item2 = None
        self.headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://www.wei-liu.com",
    "pragma": "no-cache",
    "referer": "https://www.wei-liu.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
        self.ctx = execjs.compile(open('01-xl-微流云.js',encoding='utf-8').read())

    def login1(self):
        url = 'https://api.wei-liu.com/api/v1/Token/code'
        res = requests.get(url)
        self.item1 = res.json().get('data')['item1']
        self.item2 = res.json().get('data')['item2']

    def login2(self):
        url = 'https://api.wei-liu.com/api/v1/Token'
        pwd = self.ctx.call('get_pwd','123456',self.item1,self.item2)
        data = {
            "code": "",
            "grant_type": "password",
            "language": "zh-CN",
            "password": pwd,
            "userType": "1",
            "username": "123123123"
        }
        res = requests.post(url,headers=self.headers,json=data)
        print(res.text)

    def run(self):
        self.login1()
        self.login2()

if __name__ == '__main__':
    Login().run()



