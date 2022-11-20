import json
import requests
import execjs
from loguru import logger

page  = 1 # 初始值 1page
total_page = 2  # 假设总页数

def get_data():
    global page,total_page
    while page <= total_page:
        url = 'https://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list'
        params = {'pg':str(page),
            'pgsz':'15',
            'total':'450',}
        logger.info(f'正在采集第{params["pg"]}页的数据')
        headers = {
        "Referer": "https://jzsc.mohurd.gov.cn/data/company",
        "sec-ch-ua": "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "timeout": "30000",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
        js_coed = '''
        var CryptoJS = require('crypto-js')
        d = {}
        d.a = CryptoJS
            function h(t) {
                f = d.a.enc.Utf8.parse("jo8j9wGw%6HbxfFn")
                m = d.a.enc.Utf8.parse("0123456789ABCDEF");
                var e = d.a.enc.Hex.parse(t)
                  , n = d.a.enc.Base64.stringify(e)
                  , a = d.a.AES.decrypt(n, f, {
                    iv: m,
                    mode: d.a.mode.CBC,
                    padding: d.a.pad.Pkcs7
                })
                  , r = a.toString(d.a.enc.Utf8);
                return r.toString()
            }
            
        '''
        res = requests.get(url,params=params,headers=headers)
        print(res.text)
        data = execjs.compile(js_coed).call('h',res.text)
        print('*'*100)
        print(data)
        page+=1
        items = json.loads(data)
        total = items.get('data')['total'] # 450
        total_page = int(total) / 15

if __name__ == '__main__':
    get_data()



