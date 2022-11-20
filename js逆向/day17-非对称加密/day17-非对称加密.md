## 非对称加密



### 1 非对称简介		

​		与对称加密算法不同，非对称加密算法需要两个密钥：公开密钥`（publickey）`和私有密钥`（privatekey）`。公开密钥与私有密钥是一对，如果用公开密钥对数据进行加密，只有用对应的私有密钥才能解密；如果用私有密钥对数据进行加密，那么只有用对应的公开密钥才能解密。因为加密和解密使用的是两个不同的密钥，所以这种算法叫作非对称加密算法。

- 常见非对称加密算法 `RSA`、`DSA`。
- 非对称加密算法私钥由数据接收方持有，不会在网络上传递，保证了密钥的安全。
- 非对称加密算法通常比对称加密算法计算复杂，性能消耗高。
- 非对称加密算法可用于数字签名。

![image-20220817145413422](images\image-20220817145413422.png)

**注意：**

+ 使用时都是使用公钥加密使用私钥解密，公钥可以公开，私钥自己保留。
+ 算法强度复杂、安全性依赖于算法与密钥但是由于其算法复杂，而使加密解密速度慢于对称加密

### 2 非对称特征

常见JavaScript调试算法

- 搜索关键词 `new JSEncrypt()`，`JSEncrypt` 等，一般会使用 `JSEncrypt `库，会有 new 一个实例对象的操作；
- 搜索关键词 `setPublicKey`、`setKey`、`setPrivateKey`、`getPublicKey` 等，一般实现的代码里都含有设置密钥的过程。

RSA 的私钥、公钥、明文、密文长度也有一定对应关系，也可以从这方面初步判断：

| 私钥长度 | 公钥长度 | 明文长度 | 密文长度 |
| -------- | -------- | -------- | -------- |
| 428      | 128      | 1~53     | 88       |
| 812      | 216      | 1~117    | 172      |
| 1588     | 392      | 1~245    | 344      |

#### 2.1  JavaScript 实现

```javascript
// npm install node-rsa --save
// 引用 node-rsa 加密模块
var NodeRSA = require('node-rsa');

function rsaEncrypt() {
    pubKey = new NodeRSA(publicKey,'pkcs8-public');
    var encryptedData = pubKey.encrypt(text, 'base64');
    return encryptedData
}

function rsaDecrypt() {
    priKey = new NodeRSA(privatekey,'pkcs8-private');
    var decryptedData = priKey.decrypt(encryptedData, 'utf8');
    return decryptedData
}

var key = new NodeRSA({b: 512});                    //生成512位秘钥
var publicKey = key.exportKey('pkcs8-public');    //导出公钥
var privatekey = key.exportKey('pkcs8-private');  //导出私钥
var text = "I love Python!"

var encryptedData = rsaEncrypt()
var decryptedData = rsaDecrypt()

console.log("公钥:\n", publicKey)
console.log("私钥:\n", privatekey)
console.log("加密字符串: ", encryptedData)
console.log("解密字符串: ", decryptedData)
```

#### 2.2 Python 实现

模块：`rsa`

```python
# -*- coding: utf-8 -*-
# @Author  : 夏洛
# @File    : 02-demo.py
# @VX : tl210329
import rsa
import base64

def rsa_encrypt(pu_key, t):
    # 公钥加密
    rsas = rsa.encrypt(t.encode("utf-8"), pu_key)
    return base64.b64encode(rsas)

def rsa_decrypt(pr_key, t):
    # 私钥解密
    rsas = rsa.decrypt(base64.b64decode(t), pr_key).decode("utf-8")
    return rsas

if __name__ == "__main__":
    public_key, private_key = rsa.newkeys(512)   # 生成公钥、私钥
    print('公钥：', public_key)
    print('私钥：', private_key)
    text = 'I love Python!'  # 加密对象
    encrypted_str = rsa_encrypt(public_key, text)
    print('加密字符串：', encrypted_str)
    decrypted_str = rsa_decrypt(private_key, encrypted_str)
    print('解密字符串：', decrypted_str)
```



### 3 案例实战

- 目标：房天下账号密码登录

- 主页：https://passport.fang.com/

- 接口：https://passport.fang.com/login.api

- 逆向参数：

  **Form Data：**

  ```python
  pwd: 044b527dba64d1e82657668beae1d61e4d86643d231792c78d5c538461a146b01c8e28d98b14915a11758deb60
  ```

#### 3.1 抓包分析

随便输入一个账号密码，点击登陆，抓包定位到登录接口为 https://passport.fang.com/login.api ，POST 请求，`Form Data` 里，密码 `pwd` 被加密处理了。



![图片](https://mmbiz.qpic.cn/mmbiz_png/iabtD4jabia4JSlhKbZ7886IyfdWMia07OD7Tiad5l19Et3lneVcJf9Mq5hjibB7aibSAKQLXNTiaWicbUicaD6QNUrG4pA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

#### 3.2 参数逆向

加密参数只有一个 pwd，直接全局搜索，出现一个 `loginbypassword.js`，很明显就是加密的` JS`，这个` JS `贴心的写上了中文注释，直接来到登录模块，埋下断点：



![图片](https://mmbiz.qpic.cn/mmbiz_png/iabtD4jabia4JSlhKbZ7886IyfdWMia07OD10Ws71Y2XXPYuibSyN8Dibv6At2ppLBgYX45ZEEfxRz1Zm66AjByaShA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)



**关键代码：**

```python
uid: that.username.val(),
pwd: encryptedString(key_to_encode, that.password.val()),
Service: that.service.val(),
AutoLogin: that.autoLogin.val()
```



这里主要用到了 `encryptedString` 这个函数和 `key_to_encode` 参数，鼠标放到` encryptedString` 函数上面，可以看到这个函数实际上是在一个叫做 `RSA.min.js` 的加密 JS 文件里，很明显的` RSA `加密，我们跟进这个函数，直接将所有加密函数剥离下来进行本地调试即可：



![图片](https://mmbiz.qpic.cn/mmbiz_png/iabtD4jabia4IyXASUYVZqIEibOcJqWTkv3hcibJ0AqYiczRQ4ZKlpcIYKFAibH0uscqZgHI4xlaV2oPJlK4Oy5ST4Ww/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)



而 `key_to_encode` 这个参数是可以直接在首页搜到，可以看到是向 `RSAKeyPair` 函数传入参数得到的：



![图片](https://mmbiz.qpic.cn/mmbiz_png/iabtD4jabia4JSlhKbZ7886IyfdWMia07ODqWBOylQdaQQRfPN9YU4A64DtmaibLVW4jVP1BKLGicKlWibZ84hjpDGLQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)



根据以上分析，我们可以把加密的主要步骤重写并封装成一个函数：

```python
function getEncryptedPassword(pwd, n, i, t) {
    var key_to_encode = new RSAKeyPair(n, i, t);
    return encryptedString(key_to_encode, pwd)
}
```

其中` pwd` 就是明文密码，`n，i，t` 是用来获取 `key_to_encode` 的参数，它们三个的值都可以在主页中找到。

#### 3.3 JS代码

+ `setMaxDigits()`貌似是生成密文的最大位数， 计算公式` n ** 2 / 16`。其中n为密钥长度

```javascript
function setMaxDigits(n) {}

function BigInt(n) {}

function biFromDecimal(n) {}

// 此处省略 N 个函数

function twoDigit(n) {}

function encryptedString(n, t) {}

function decryptedString(n, t) {}

var biRadixBase = 2, biRadixBits = 16, bitsPerDigit = biRadixBits, biRadix = 65536, biHalfRadix = biRadix >>> 1,
    biRadixSquared = biRadix * biRadix, maxDigitVal = biRadix - 1, maxInteger = 9999999999999998, maxDigits, ZERO_ARRAY,
    bigZero, bigOne, dpl10, lr10, hexatrigesimalToChar, hexToChar, highBitMasks, lowBitMasks;
setMaxDigits(20);
dpl10 = 15;
lr10 = biFromNumber(1e15);
hexatrigesimalToChar = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
hexToChar = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"];
highBitMasks = [0, 32768, 49152, 57344, 61440, 63488, 64512, 65024, 65280, 65408, 65472, 65504, 65520, 65528, 65532, 65534, 65535];
lowBitMasks = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535];
setMaxDigits(129);

function getEncryptedPassword(pwd, n, i, t) {
    var key_to_encode = new RSAKeyPair(n, i, t);
    return encryptedString(key_to_encode, pwd)
}

// 测试样例
// console.log(getEncryptedPassword("16521689404", "010001", "", "978C0A92D2173439707498F0944AA476B1B62595877DD6FA87F6E2AC6DCB3D0BF0B82857439C99B5091192BC134889DFF60C562EC54EFBA4FF2F9D55ADBCCEA4A2FBA80CB398ED501280A007C83AF30C3D1A142D6133C63012B90AB26AC60C898FB66EDC3192C3EC4FF66925A64003B72496099F4F09A9FB72A2CF9E4D770C41"))
```



#### 3.4 python代码

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import execjs
import requests


index_url = 'https://passport.fang.com/'
login_url = 'https://passport.fang.com/login.api'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
session = requests.session()


def get_key_to_encode():
    headers = {'User-Agent': user_agent}
    response = session.get(url=index_url, headers=headers)
    key_to_encode = re.findall(r'RSAKeyPair\((.*)\);', response.text)[0].replace('"', '').split(', ')
    return key_to_encode


def get_encrypted_password(key_to_encode, pwd):
    n, i, t = key_to_encode[0], key_to_encode[1], key_to_encode[2]
    with open('fang_encrypt.js', 'r', encoding='utf-8') as f:
        fang_js = f.read()
    encrypted_pwd = execjs.compile(fang_js).call('getEncryptedPassword', pwd, n, i, t)
    return encrypted_pwd


def login(encrypted_password, uid):
    headers = {
        'User-Agent': user_agent,
        'X-Requested-With': 'XMLHttpRequest',
        'Host': 'passport.fang.com',
        'Origin': 'https://passport.fang.com',
        'Referer': 'https://passport.fang.com/?backurl=http%3a%2f%2fmy.fang.com%2f',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    data = {
        'uid': uid,
        'pwd': encrypted_password,
        'Service': 'soufun-passport-web',
        'AutoLogin': 1
    }
    response = session.post(url=login_url, data=data, headers=headers)
    print(response.json())


def main():
    # 16521689404
    uid = input('请输入登录账号：')
    pwd = input('请输入登录密码：')
    rsa_key = get_key_to_encode()
    encrypted_pwd = get_encrypted_password(rsa_key, pwd)
    login(encrypted_pwd, uid)


if __name__ == '__main__':
    main()
```



### 4. 案例实战

**说明**

```text
本教程为教学使用，不承担任何风险，请各学员自觉遵守法律法规 -- 微流云平台
```

#### 4.1 逆向参数

+ 该案例是多层嵌套加密

```python
地址：https://www.wei-liu.com/user/login.html

password: "ZfYhxYg6V6STQDo8FwTCeqpmtsWjh73R/nIotCh0RnkuJMgd7e72U+JVo/XQ6sY3qEVd+J+d6D
```



#### 4.2 逆向分析

点击登录会加载2个地址

地址1：https://api.wei-liu.com/api/v1/Token/code

地址2：https://api.wei-liu.com/api/v1/Token

**总结：**地址2里面有携带参数  地址1返回`公钥`和`item2`参数

#### 4.3 JavaScript分析

![image-20220817153828723](images\image-20220817153828723.png)



**总结：**从这里可以看出密码是属于加密的

下`XHR`断点分析`https://api.wei-liu.com/api/v1/Token`,可以在以下位置发现参数

![image-20220817154256383](images\image-20220817154256383.png)



#### 4.4 密钥分析

+ 拉动滑块，获取后台公钥 `item1` 和带有时间的`item2`

![image-20220817153949071](images\image-20220817153949071.png)

#### 4.5 算法还原

##### 4.5.1 用python模拟请求测试

```python
def get_miyue():
    session = requests.session()
    header = {
        '具体参数找夏洛老师拿'
    }
    session.headers = header
    url = 'https://api.wei-liu.com/api/v1/Token/code'
    res = session.get(url)
    if res.status_code == 200:
        res1 = res.json().get('data')
        item1 = res1.get('item1')
        item2 = res1.get('item2')
        return item1,item2
```

##### 4.5.2  JavaScript测试代码

```javascript
JSEncrypt = require('jsencrypt');
function encrypt(module,pubCode,pwd){
	var encrypt = new JSEncrypt();
    encrypt.setPublicKey(module);
    var result = encrypt.encrypt(pubCode + pwd);
    return result;
}
```

##### 4.5.3 密码获取

```javascript
js_code = open('psd.js','r').read()
result = execjs.compile(js_code).call('encrypt',item1,item2,jm_sha256(''))
```



