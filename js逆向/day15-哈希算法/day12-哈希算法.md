## 摘要算法

在 `JavaScript` 中和 `Python `中的基本实现方法，遇到 `JS` 加密的时候可以快速还原加密过程，有的网站在加密的过程中可能还经过了其他处理，但是大致的方法是一样的。

消息摘要算法/签名算法：`MD5、SHA、HMAC`

### 1. MD5

简介：全称` MD5` 消息摘要算法，又称哈希算法、散列算法，由美国密码学家`罗纳德·李维斯特`设计，于 1992 年作为 RFC 1321 被公布，用以取代 MD4 算法。摘要算法是单向加密的，也就是说明文通过摘要算法加密之后，是不能解密的。摘要算法的第二个特点密文是固定长度的，它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用`16进制`的字符串表示）。之所以叫摘要算法，它的算法就是提取明文重要的特征。所以，两个不同的明文，使用了摘要算法之后，有可能他们的密文是一样的，不过这个概率非常的低。

#### 1.1 JavaScript 实现

地址：https://www.autohome.com.cn/changsha/

安装对应的模块

```javascript
npm install crypto-js  --save
```

**使用案例**

```JavaScript
// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function MD5Test() {
    var text = "I love python!"
    return CryptoJS.MD5(text).toString()
}

console.log(MD5Test())  // 21169ee3acd4a24e1fcb4322cfd9a2b8
```

#### 1.2 Python 实现

```python
import hashlib

def md5_test2():
    md5 = hashlib.md5()
    md5.update('python'.encode('utf-8'))
    print(md5.hexdigest())

if __name__ == '__main__':
    md5_test2()  # 21169ee3acd4a24e1fcb4322cfd9a2b8
```

**总结：**`MD5`哈希视为字符串，而是将其视为十六进制数， `MD5`哈希长度为128位，通常由`32`个十六进制数字表示。



### 2. SHA

简介：全称安全哈希算法，由美国国家安全局`（NSA）`所设计，主要适用于数字签名标准里面定义的数字签名算法，`SHA` 通常指 `SHA` 家族的五个算法，分别是` SHA-1、SHA-224、SHA-256、SHA-384、SHA-512`，`SHA` 是比 `MD5` 更安全一点的摘要算法，`MD5` 的密文是 32 位，而 `SHA-1` 是 40 位，版本越强，密文越长，代价是速度越慢。

#### 2.1  JavaScript 实现

```JavaScript
// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function SHA1Encrypt() {
    var text = "I love python!"
    return CryptoJS.SHA1(text).toString();
}

console.log(SHA1Encrypt())  // 23c02b203bd2e2ca19da911f1d270a06d86719fb
```

#### 2.2 Python 实现

```python
import hashlib

def sha1_test2():
    sha1 = hashlib.sha1()
    sha1.update('I love python!'.encode('utf-8'))
    print(sha1.hexdigest())

if __name__ == '__main__':
    sha1_test2()  # 23c02b203bd2e2ca19da911f1d270a06d86719fb
```



### 3. `HMAC`

简介：全称散列消息认证码、密钥相关的哈希运算消息认证码，于 1996 年提出，1997 年作为 RFC 2104 被公布，`HMAC` 加密算法是一种安全的基于加密 `Hash` 函数和共享密钥的消息认证协议，它要求通信双方共享密钥 key、约定算法、对报文进行 `Hash` 运算，形成固定长度的认证码。通信双方通过认证码的校验来确定报文的合法性。

参考资料：

- 百科：https://baike.baidu.com/item/hmac/7307543?fr=aladdin

#### 3.1 JavaScript 实现

```JavaScript
// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function HMACEncrypt() {
    var text = "I love python!"
    var key = "secret"   // 密钥文件
    return CryptoJS.HmacMD5(text, key).toString();
    // return CryptoJS.HmacSHA1(text, key).toString();
    // return CryptoJS.HmacSHA256(text, key).toString();
}
console.log(HMACEncrypt())
```

#### 3.2 Python 实现

```python
import hmac

def hmac_test1():
    message = b'I love python!'
    key = b'secret'
    md5 = hmac.new(key, message, digestmod='MD5')
    print(md5.hexdigest())


def hmac_test2():
    key = 'secret'.encode('utf8')
    sha1 = hmac.new(key, digestmod='sha1')
    sha1.update('I love '.encode('utf8'))
    sha1.update('Python!'.encode('utf8'))
    print(sha1.hexdigest())

if __name__ == '__main__':
    hmac_test1()  # 9c503a1f852edcc3526ea56976c38edf
    hmac_test2()  # 2d8449a4292d4bbeed99ce9ea570880d6e19b61a
```

### 4. 实战案例

#### 4.1 案例 `md5`加密逆向

##### 4.1.1 **逆向目标**

+ 主页：http://fanyi.youdao.com/

+ 逆向字段：`sign: 'asdasdasdasdasdasdasd'`

##### 4.1.2 **逆向分析**

1.  先进行抓包，可以看到有一个签名信息 `sign`

![image-20220815140510538](images\image-20220815140510538.png)



2.  数据加密位置，可以在这儿进行分析

![image-20220815141402089](images\image-20220815141402089.png)



##### 4.1.3 **python代码模拟**

```python
# encoding: utf-8
"""
@author: 夏洛
@QQ: 1972386194
@site: https://www.tulingxueyuan.cn/
@file: 网易云.py
"""
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

```



#### 4.2 案例`sha256`系列

**逆向目标**

+ 主页：http://www.hh1024.com/

+ 接口：https://ucp.hrdjyun.com:60359/api/dy

+ 逆向参数：`sign: "0d2864b1420c42f12de6efeff30bcb4b458157d8177675b8910fa632524604cb"`

##### 4.2.1  抓包分析：

1. 通过对比，可以发现这个参数每次都会切换

![image-20220815142259011](images\image-20220815142259011.png)



##### 4.2.2 调试加密地地点

1. 打开全局搜索 `sign`关键字

![image-20220815143019563](images\image-20220815143019563.png)

2. 参数加密地点

![image-20220815143143609](images\image-20220815143143609.png)



##### 4.2.3 python代码实现

```python
import urllib3,requests,time,json
urllib3.disable_warnings()
import hashlib

months = input("请输入查询月份：")
days = input("请输入查询日期,2天以内：")
times = str(int(time.time()) * 1000)
params = {"no":"dy0002","data":{"days":1,"rankType":5,"liveDay":f"2022-{months.zfill(2)}-{days.zfill(2)}"}}
print(params)
dd = json.dumps(params)
def get_sign():
    data = f'param={dd}&timestamp={times}&tenant=1&salt=kbn%&)@<?FGkfs8sdf4Vg1*+;`kf5ndl$'  # 要进行加密的数据
    data_sha = hashlib.sha256(data.encode('utf-8')).hexdigest()
    return data_sha

def get_data():
    s = get_sign()
    datas = {"param":dd,"sign":s,"tenant":"1","timestamp":times,"token":t}
    url = 'https://ucp.hrdjyun.com:60359/api/dy'
    res = session.post(url,headers=headers,data=json.dumps(datas))
    if res.json().get('status') == 0:
        data = res.json().get('data')['rankList']
        for d in data:
            items = {}
            items['抖音名'] = d.get('anchorName')
            items['带货销量'] ='%.2f' % (d.get('salesVolume') / 10000) + '万'
            items['带货销售额'] = '%.2f' % (d.get('salesMoney') / 1000000) + '万'
            items['粉丝'] = '%.2f' % (d.get('fans') / 10000) + '万'
            items['在线人数'] = '%.2f' % (d.get('online') / 10000) + '万'
            items['时间']  =d.get('liveDay')
            print(items)


if __name__ == '__main__':
    reads = """
        本接口只开放抖音带货销量日榜
        可以根据日期查询
                                --- 夏洛
        """
    print(reads)
    get_data()
```



   





​    

