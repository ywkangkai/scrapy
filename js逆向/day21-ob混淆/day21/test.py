

import execjs
ctll = execjs.compile(open('产业数据.js',encoding='utf-8').read())
data = {
    "policyType": "6",
    "province": "",
    "city": "",
    "downtown": "",
    "garden": "",
    "centralId": "",
    "sort": 0,
    "pageNum": 1,
    "pageSize": 7
}
par = ctll.call('xl',data)
# python传参 记得改这个就可以了
print(bytes(par.get('data')))
# requests.post(url,data=bytes(par.get('data')),headers=headers)
