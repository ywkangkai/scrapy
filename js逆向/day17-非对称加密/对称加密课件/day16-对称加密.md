## 对称加密

对称加密（加密解密密钥相同）：DES、3DES、AES、RC4



**简介**

对称式加密就是加密和解密使用同一个密钥。信息接收双方都需事先知道密匙和加解密算法且其密匙是相同的，之后便是对数据进行加解密了。对称加密算法用来对敏感数据等信息进行加密。

![image-20220816202802353](images\image-20220816202802353.png)



### 常见算法归纳

DES：56位密钥，由于密钥太短，被逐渐被弃用。

AES：有128位、192位、256位密钥，现在比较流行。密钥长、可以增加破解的难度和成本。



### 1. DES算法

![image-20221116133758840](images\image-20221116133758840.png)

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



#### 2.3 实际案例

##### 2.3.1 逆向目标

- 目标：建筑市场数据采集

- 主页：https://jzsc.mohurd.gov.cn/data/company

- 接口：https://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list

- 逆向参数：`data加密`


##### 2.3.2 **抓包分析**

**1、抓包处理**

![image-20221118143459256](images\image-20221118143459256.png)

根据抓包结果可以分析，此接口数据是`16`进制编码的数据，如果需要采集，就需要使用算法进行分析

2、对于数据加密的网站，先看启动器分析`JS`文件，然后全局搜索`json.parse(`,一般后台返回的加密数据，会进行类型转换。



![image-20221118143437038](images\image-20221118143437038.png)

**3、数据确认**

![image-20221118144020008](images\image-20221118144020008.png)

从这里可以发现`t.data` 是后台返回的数据，`h` 是`JavaScript`里面的方法，数据经过`h`变成了明文，所以需要先分析`h`方法

**4、`h`函数判断**

![image-20221118144201390](images\image-20221118144201390.png)

经过查看分析，`h`方法是一个算法 ，可以先使用标准算法进行尝试处理

##### 2.3.3 **逆向结果**

```javascript
var CryptoJS = require('crypto-js');

    function  h(t) {

      f = CryptoJS.enc.Utf8.parse("jo8j9wGw%6HbxfFn")
      m = CryptoJS.enc.Utf8.parse("0123456789ABCDEF");

      var key = e = CryptoJS.enc.Hex.parse(t)
        n = CryptoJS.enc.Base64.stringify(e)

      var decrypt = CryptoJS.AES.decrypt(n, f,{
            iv: m,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
      });
      return  decrypt.toString(CryptoJS.enc.Utf8).toString();
    }
```









