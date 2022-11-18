## 对称加密

对称加密（加密解密密钥相同）：DES、3DES、AES、RC4



**简介**

对称式加密就是加密和解密使用同一个密钥。信息接收双方都需事先知道密匙和加解密算法且其密匙是相同的，之后便是对数据进行加解密了。对称加密算法用来对敏感数据等信息进行加密。

![image-20220816202802353](images\image-20220816202802353.png)



### 常见算法归纳

DES：56位密钥，由于密钥太短，被逐渐被弃用。

AES：有128位、192位、256位密钥，现在比较流行。密钥长、可以增加破解的难度和成本。



### 1. DES算法

![image-20221116133758840](C:\Users\XL\AppData\Roaming\Typora\typora-user-images\image-20221116133758840.png)

简介：**DES**是一种分组**加密算法**，他以`64`位为分组对数据加密。`64`位一组的明文从算法的一端 输入，`64`位的密文从另一端输出。**DES**是一个对称算法：加密和解密用的是同一个算法（除 密钥编排不同以外）。

 密钥的长度为`56`位(密钥通常表示为`64`位的数，但每个第8位都用作奇偶检验，可以忽 略)。密钥可以是任意的`56`位数，且可以在任意的时候改变。

**DES**算法的入口参数有3个：`Key，Data，Mode`。其中`Key`为8个字节共64位，是**DES**算法 的工作密钥；`Data`也为8个字节64位，是要被加密或解密的数据：Mode为**DES**的工作方式，有 两种：加密或解密。

 DES算法的工作过程：若Mode为加密，则用Key对数据Data进行加密，生成Data的密码 形式（64位）作为DES的输出结果；若Mode为解密，则用Key对密码形式的数据Data解密，还 原为Data的明码形式（64位）作为DES的输出结果。
　　 简单地说，算法只不过是加密的一种基本技术，DES基本组建分组是这些技术的一种组合 ，他基于密钥作用于明文，这是众所周知的轮（round）。DES有16轮，这意味着要在明文分 组上16次实施相同的组合技术。

- mode 支持：CBC，CFB，CTR，CTRGladman，ECB，OFB 等。
- padding 支持：ZeroPadding，NoPadding，AnsiX923，Iso10126，Iso97971，Pkcs7 等。



**工作模式归纳**

- **ECB模式** 全称Electronic Codebook模式，译为电子密码本模式

- **CBC模式** 全称Cipher Block Chaining模式，译为密文分组链接模式

- **CFB模式** 全称Cipher FeedBack模式，译为密文反馈模式

- **OFB模式** 全称Output Feedback模式，译为输出反馈模式。

- **CTR模式** 全称Counter模式，译为计数器模式。


iv: 防止同样的明文块、加密成同样的密文块

**参考资料：**

- RFC 4772：https://datatracker.ietf.org/doc/rfc4772/
- DES 维基百科：https://en.wikipedia.org/wiki/Data_Encryption_Standard

#### 1.1 JavaScript 实现

`DES`算法的入口参数有3个

+ `key、DATA、Mode、padding`
  + `key`为`7个字节`共56位，是DES算法的工作密钥
  + `Data`为`8个字节`64位，是要被加密或被解密的数据
  + `Mode`为`DES`的工作方式
  + `padding`为填充模式，如果加密后密文长度如果达不到指定整数倍（8个字节，16个字节），填充

```JavaScript
// 引用 crypto-js 加密模块 
var CryptoJS = require('crypto-js')

function desEncrypt() {
    var key = CryptoJS.enc.Utf8.parse(desKey),
        iv = CryptoJS.enc.Utf8.parse(desIv),
        srcs = CryptoJS.enc.Utf8.parse(text),
        // CBC 加密模式，Pkcs7 填充方式
        encrypted = CryptoJS.DES.encrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
    return encrypted.toString();
}

function desDecrypt() {
    var key = CryptoJS.enc.Utf8.parse(desKey),
        iv = CryptoJS.enc.Utf8.parse(desIv),
        srcs = encryptedData,
        // CBC 加密模式，Pkcs7 填充方式
        decrypted = CryptoJS.DES.decrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
    return decrypted.toString(CryptoJS.enc.Utf8);
}

var text = "I love Python!"       // 待加密对象
var desKey = "6f726c64f2c2057"    // 密钥
var desIv = "0123456789ABCDEF"    // 初始向量

var encryptedData = desEncrypt()
var decryptedData = desDecrypt()

console.log("加密字符串: ", encryptedData)
console.log("解密字符串: ", decryptedData)

// 加密字符串:  +ndbEkWNw2QAfIYQtwC14w==
// 解密字符串:  I love Python!
```



#### 1.2 Python 实现

```python
pip install pyDes
```



```python
import binascii
# 加密模式 CBC，填充方式 PAD_PKCS5
from pyDes import des, CBC, PAD_PKCS5

def des_encrypt(key, text, iv):
    k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(text, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)

def des_decrypt(key, text, iv):
    k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(text), padmode=PAD_PKCS5)
    return de

if __name__ == '__main__':
    secret_key = '12345678'   # 密钥
    text = 'hello world'   # 加密对象
    iv = secret_key           # 偏移量
    secret_str = des_encrypt(secret_key, text, iv)
    print('加密字符串：', secret_str)
    clear_str = des_decrypt(secret_key, secret_str, iv)
    print('解密字符串：', clear_str)


# 加密字符串：b'302d3abf2421169239f829b38a9545f1'
# 解密字符串：b'I love Python!'
```

总结：https://www.processon.com/view/link/6374f0e10e3e742ce7bd597b



#### 1.3 实操练习1

地址：https://bqcm0.cavip1.com/

地址：http://www.91118.com/Passport/Account/Login



#### 1.4 实操练习2

##### 1.3.1 逆向目标

首页：https://www.endata.com.cn/BoxOffice/BO/Month/oneMonth.html

数据：https://www.endata.com.cn/API/GetData.ashx

逆向：加密数据

##### 1.3.2 逆向分析

+ 使用xhr断点数据地址，进行单步调试

![image-20220816214111191](images\image-20220816214111191.png)

+ 调试对应的数据

![image-20220816214102754](images\image-20220816214102754.png)

总结：可以看到他是对数据用`webInstace.shell`进行了解密

##### 1.3.3  数据还原

```javascript

```

### 2. AES算法

**环境安装**

```python
pip install pycryptodome -i pip源
```

#### 2.1 算法简介

​		简介：全称高级加密标准（英文名称：Advanced Encryption Standard），在密码学中又称 Rijndael 加密法，由美国国家标准与技术研究院 （NIST）于 2001 年发布，并在 2002 年成为有效的标准，是美国联邦政府采用的一种区块加密标准。这个标准用来替代原先的 DES，已经被多方分析且广为全世界所使用，它本身只有一个密钥，即用来实现加密，也用于解密。

- mode 支持：CBC，CFB，CTR，CTRGladman，ECB，OFB 等。
- padding 支持：ZeroPadding，NoPadding，AnsiX923，Iso10126，Iso97971，Pkcs7 等。

**参考资料：**

- RFC 3268：https://datatracker.ietf.org/doc/rfc3268/
- AES 维基百科：https://en.wikipedia.org/wiki/Advanced_Encryption_Standard



**参数定义：**

1. key length（密钥位数，密码长度）`AES128，AES192，AES256（128 位、192 位或 256 位）`
2. key （密钥，密码）key指的就是密码了，`AES128`就是`128位`的，如果位数不够，某些库可能会自动填充到`128`。
3. IV （向量）IV称为初始向量，不同的IV加密后的字符串是不同的，加密和解密需要相同的IV。
4. mode （加密模式）AES分为几种模式，比如ECB，CBC，CFB等等，这些模式除了ECB由于没有使用IV而不太安全，其他模式差别并没有太明显。
5. padding （填充方式）对于加密解密两端需要使用同一的PADDING模式，大部分PADDING模式为`PKCS5, PKCS7, NOPADDING`。

**加密原理：**

​		AES加密算法采用分组密码体制，每个分组数据的长度为`128位16个字节`，密钥长度可以是`128位16个字节`、`192位或256位`，一共有四种加密模式，我们通常采用需要初始向量IV的CBC模式，初始向量的长度也是`128位16个字节`。

#### 2.2  JavaScript 实现

类似网站：https://www.dns.com/login.html

```javascript
// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function tripleAesEncrypt() {
    var key = CryptoJS.enc.Utf8.parse(aesKey),
        iv = CryptoJS.enc.Utf8.parse(aesIv),
        srcs = CryptoJS.enc.Utf8.parse(text),
        // CBC 加密方式，Pkcs7 填充方式
        encrypted = CryptoJS.AES.encrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
    return encrypted.toString();
}

function tripleAesDecrypt() {
    var key = CryptoJS.enc.Utf8.parse(aesKey),
        iv = CryptoJS.enc.Utf8.parse(aesIv),
        srcs = encryptedData,
        // CBC 加密方式，Pkcs7 填充方式
        decrypted = CryptoJS.AES.decrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
    return decrypted.toString(CryptoJS.enc.Utf8);
}

var text = "I love Python!"       // 待加密对象
var aesKey = "6f726c64f2c2057c"   // 密钥，16 倍数
var aesIv = "0123456789ABCDEF"    // 偏移量，16 倍数

var encryptedData = tripleAesEncrypt()
var decryptedData = tripleAesDecrypt()

console.log("加密字符串: ", encryptedData)
console.log("解密字符串: ", decryptedData)

// 加密字符串:  dZL7TLJR786VGvuUvqYGoQ==
// 解密字符串:  I love Python!
```

#### 2.3 Python 实现

```python
import base64
from Crypto.Cipher import AES

# 需要补位，str不是16的倍数那就补足为16的倍数
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)


# 加密方法
def aes_encrypt(key, t, iv):
    aes = AES.new(add_to_16(key), AES.MODE_CBC, add_to_16(iv))  # 初始化加密器
    encrypt_aes = aes.encrypt(add_to_16(t))                    # 先进行 aes 加密
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回 bytes
    return encrypted_text


# 解密方法
def aes_decrypt(key, t, iv):
    aes = AES.new(add_to_16(key), AES.MODE_CBC, add_to_16(iv))         # 初始化加密器
    base64_decrypted = base64.decodebytes(t.encode(encoding='utf-8'))  # 优先逆向解密 base64 成 bytes
    decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')  # 执行解密密并转码返回str
    return decrypted_text


if __name__ == '__main__':
    secret_key = '12345678'   # 密钥
    text = 'I love Python!'   # 加密对象
    iv = secret_key           # 初始向量
    encrypted_str = aes_encrypt(secret_key, text, iv)
    print('加密字符串：', encrypted_str)
    decrypted_str = aes_decrypt(secret_key, encrypted_str, iv)
    print('解密字符串：', decrypted_str)


# 加密字符串：lAVKvkQh+GtdNpoKf4/mHA==
# 解密字符串：I love Python!
```

**注意：**明文加密要求是16的整数倍

#### 2.4 实际案例

##### 2.4.1 逆向目标

- 目标：升学E网通登录接口

- 主页：https://web.ewt360.com/register/#/login

- 接口：aHR0cHM6Ly9nYXRld2F5LmV3dDM2MC5jb20vYXBpL2F1dGhjZW50ZXIvdjIvb2F1dGgvbG9naW4vYWNjb3VudA==

- 逆向参数：

- - Request Headers：`sign: 3976F10977FC65F9CB967AEF79E508BD`
  - Request Payload：`password: "A7428361DEF118911783F446A129FFCE"`

##### 2.4.2 **抓包分析**

来到某 e 网通的登录页面，随便输入一个账号密码登陆，抓包定位到登录接口为 aHR0cHM6Ly9nYXRld2F5LmV3dDM2MC5jb20vYXBpL2F1dGhjZW50ZXIvdjIvb2F1dGgvbG9naW4vYWNjb3VudA==，请求头里，有一个 sign，Payload 里，密码 password 被加密处理了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/iabtD4jabia4LJmLPiaJcQvictOzV5grPjHoZNhkpZPBpU6tz4mqWoTJtXFQZKhfkTvSialn6ibj0yBicyiaZbIhVZtCPw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

##### 2.4.3 **参数逆向**

###### 2.4.3 sign签名处理

首先来看一下请求头的 sign，尝试直接搜索一下，发现并不是经过某些请求返回的数据，观察一下其他请求，可以发现同样有 sign，而且每次请求的值都不一样：

![图片](https://mmbiz.qpic.cn/mmbiz_png/iabtD4jabia4LJmLPiaJcQvictOzV5grPjHoMDx6z4kPU6VhTuibYUBdXeVQFhFldMuklxpSL2DJygc8lMibR9O5sMdQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

由此可以初步判断这个值应该是通过 JS 生成的，全局搜索关键字 `sign:`，可以分别在 request.js、request.ts 两个文件里面看到疑似 sign 赋值的地方，埋下断点调试，成功断下，原理也很简单，时间戳加上一串固定的字符，经过 MD5 加密后再转大写即可。

![图片](https://mmbiz.qpic.cn/mmbiz_png/iabtD4jabia4LJmLPiaJcQvictOzV5grPjHoicnFVj3zL44ojiavuibLpXEuQdAqkqgNgdFW1IdtQnzehZpvpcCiclMyqQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**使用 Python 实现：**

```python
import time
import hashlib

timestamp = str(int(time.time() * 1000))
sign = hashlib.md5((timestamp + 'bdc739ff2dcf').encode(encoding='utf-8')).hexdigest().upper()
print(sign)
```

###### 2.4.4 password处理

​		`password` 是明文密码经过加密后得到的值，如果尝试直接去搜索的话，会发现出来的值非常非常多，要想找到准确的值难度巨大：

可以看到这条请求是 XHR 请求，本次我们使用 `XHR` 断点的方法来定位具体的加密位置，通过本次案例，我们来学习一下具体是如何跟进调用栈、如何通过上下文来定位具体的加密位置。

切换到 `Network` 选项卡，找到登陆请求，鼠标移动到 `Initiator` 选项卡下的 JS 上，可以看到其调用栈，如果站点的加密方式比较简单，没有太多混淆的话，调用栈里面就可以看到` login、send、post、encrypt` 等等之类的关键词，这种情况下就可以直接点进去，比较容易找到加密的地方，但是大多数站点对于函数名、变量名都做了混淆，和本案例一样，调用栈里面显示的都是一些单个或者多个无规则的字母的函数，无法直接定位，此时就需要我们从最后一个函数往前慢慢找。

![图片](https://mmbiz.qpic.cn/mmbiz_png/iabtD4jabia4LJmLPiaJcQvictOzV5grPjHoOsRR2ZTwG6rNG2iagDu7fVZ7zZ1R2FVFrUbjvsbSKl29RepPYply00w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

点击进入最后一个函数，即 Y 函数，它位于调用栈的最顶层，表示经过此函数后，浏览器就会发送登录的请求，密码的加密过程已经处理完毕。在此函数埋下断点，可以在右侧的` Call Stack` 看到调用栈，从下到上，表示的是点击登陆后，先后调用的函数的执行过程：

![图片](https://mmbiz.qpic.cn/mmbiz_png/iabtD4jabia4LJmLPiaJcQvictOzV5grPjHo2WIZ1rEprQow9ne8xmILRodRYLltcQ1Na0DOGOFSmrRPPITSSkG9eA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

根据这种思路，一步一步往下跟进调用栈，可以看到在 utils.ts 里面执行了一个匿名函数，其中调用了一个 passwordEncrypt 函数，通过函数名就可以看出基本上就是密码加密的函数了：

**总结：**

在此处埋下断点进行调试，传进来的是明文密码，passwordEncrypt 实际上是调用的 encode.ts 中的 O 函数：

跟进 O 函数，引用了 crypto-js 加密模块，很明显的 AES 加密，本地改写一下就行了。



**JavaScript 加密代码**

```javascript
CryptoJS = require("crypto-js")

const key = CryptoJS.enc.Utf8.parse("20171109124536982017110912453698");
const iv = CryptoJS.enc.Utf8.parse('2017110912453698'); //十六位十六进制数作为密钥偏移量

function getEncryptedPassword(word) {
    let srcs = CryptoJS.enc.Utf8.parse(word);
    let encrypted = CryptoJS.AES.encrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
    return encrypted.ciphertext.toString().toUpperCase();
}

// 测试样例
// console.log(getEncryptedPassword("123457"))
```



python模拟登录

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import hashlib
import execjs
import requests


login_url = 'https://gateway.ewt360.com/api/authcenter/v2/oauth/login/account'
session = requests.session()

def get_sign():
    timestamp = str(int(time.time()*1000))
    sign = hashlib.md5((timestamp + 'bdc739ff2dcf').encode(encoding='utf-8')).hexdigest().upper()
    return sign


def get_encrypted_parameter(password):
    with open('encrypt.js', 'r', encoding='utf-8') as f:
        ewt360_js = f.read()
    encrypted_password = execjs.compile(ewt360_js).call('getEncryptedPassword', password)
    return encrypted_password


def login(sign, username, encrypted_password):
    headers = {
        'sign': sign,
        'timestamp': str(int(time.time()*1000)),
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    data = {
        'autoLogin': True,
        'password': encrypted_password,
        'platform': 1,
        'userName': username
    }
    response = session.post(url=login_url, headers=headers, json=data)
    print(response.json())


def main():
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')
    sign = get_sign()
    encrypted_password = get_encrypted_parameter(password)
    login(sign, username, encrypted_password)


if __name__ == '__main__':
    main()
```







