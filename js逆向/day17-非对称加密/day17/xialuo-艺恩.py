
import requests
import execjs

def get_data():
    headers = {
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
    data = {
    "startTime": "2022-11-01",
    "MethodName": "BoxOffice_GetMonthBox"
}
    res = requests.post('https://www.endata.com.cn/API/GetData.ashx',data=data,headers=headers)
    print(res.text)
    response = execjs.compile(open('xialuo-艺恩.js',encoding='utf-8').read()).call('xl',res.text)
    print('*'*50)
    print(response)

if __name__ == '__main__':
   get_data()

