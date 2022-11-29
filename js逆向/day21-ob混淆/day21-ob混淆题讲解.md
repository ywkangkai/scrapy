### 令人抓狂的 JavaScript 混淆技术



### 1 JS简介

**JavaScript 压缩、混淆和加密技术**

对于网页来说，其逻辑是依赖于` JavaScript `来实现的，`JavaScript` 有如下特点：

+ `JavaScript` 代码运行于客户端，也就是它必须要在用户浏览器端加载并运行。
+ `JavaScript` 代码是公开透明的，也就是说浏览器可以直接获取到正在运行的 `JavaScript` 的源码。



**压缩、混淆、加密技术简述如下**

+ 代码压缩：即去除` JavaScript` 代码中的不必要的空格、换行等内容，使源码都压缩为几行内容，降低代码可读性，当然同时也能提高网站的加载速度。

+ 代码混淆：使用变量替换、字符串阵列化、控制流平坦化、多态变异、僵尸函数、调试保护等手段，使代码变得难以阅读和分析，达到最终保护的目的。但这不影响代码原有功能。是理想、实用的` JavaScript `保护方案

+ 代码加密：可以通过某种手段将 JavaScript 代码进行加密，转成人无法阅读或者解析的代码，如将代码完全抽象化加密，如 eval 加密。另外还有更强大的加密技术，可以直接将 `JavaScript` 代码用 C/C++ 实现，`JavaScript` 调用其编译后形成的文件来执行相应的功能，如` Emscripten` 还有 `WebAssembly`。

  

### 2 OB混淆

`OB` 混淆全称 Obfuscator，Obfuscator 其实就是混淆的意思，官网：[https://obfuscator.io/](https://links.jianshu.com/go?to=https%3A%2F%2Fobfuscator.io%2F) ，其作者是一位叫 Timofey Kachalov 的俄罗斯` JavaScript `开发工程师，早在 2016 年就发布了第一个版本。



#### 2.1 OB 混淆具有以下特征：

1、一般由一个大数组或者含有大数组的函数、一个自执行函数、解密函数和加密后的函数四部分组成；

2、函数名和变量名通常以 `_0x` 或者 `0x` 开头，后接 1~6 位数字或字母组合；

3、自执行函数，进行移位操作，有明显的 push、shift 关键字；

例如在上面的例子中，`_0x3f26()` 方法就定义了一个大数组，自执行函数里有 push、shift 关键字，主要是对大数组进行移位操作，`_0x1fe9()` 就是解密函数，`hi()` 就是加密后的函数。

![image-20220822141218145](images\image-20220822141218145.png)



#### 2.2 OB混淆介绍

​		JavaScript 混淆完全是在 JavaScript 上面进行的处理，它的目的就是使得 JavaScript 变得难以阅读和分析，大大降低代码可读性，是一种很实用的 JavaScript 保护方案。

**JavaScript 混淆技术主要有以下几种：**

+ 变量混淆
  将带有含意的变量名、方法名、常量名随机变为无意义的类乱码字符串，降低代码可读性，如转成单个字符或十六进制字符串。

+ 字符串混淆
  将字符串阵列化集中放置、并可进行 MD5 或 Base64 加密存储，使代码中不出现明文字符串，这样可以避免使用全局搜索字符串的方式定位到入口点。

+ 属性加密
  针对 JavaScript 对象的属性进行加密转化，隐藏代码之间的调用关系。

+ 控制流平坦化
  打乱函数原有代码执行流程及函数调用关系，使代码逻变得混乱无序。

+ 僵尸代码
  随机在代码中插入无用的僵尸代码、僵尸函数，进一步使代码混乱。

+ 调试保护
  基于调试器特性，对当前运行环境进行检验，加入一些强制调试 debugger 语句，使其在调试模式下难以顺利执行 JavaScript 代码。

+ 多态变异
  使 JavaScript 代码每次被调用时，将代码自身即立刻自动发生变异，变化为与之前完全不同的代码，即功能完全不变，只是代码形式变异，以此杜绝代码被动态分析调试。

+ 锁定域名
  使 JavaScript 代码只能在指定域名下执行。

+ 反格式化
  如果对 JavaScript 代码进行格式化，则无法执行，导致浏览器假死。

+ 特殊编码
  将 JavaScript 完全编码为人不可读的代码，如表情符号、特殊表示内容等等。

总之，以上方案都是 JavaScript 混淆的实现方式，可以在不同程度上保护 JavaScript 代码。



#### 2.3 OB混淆JS

新建一个文件夹，比如`feifei`，随后进入该文件夹，初始化工作空间

```js
npm init
```

提示我们输入一些信息，创建一个 package.json 文件，这就完成了项目初始化了。

接下来我们来安装 `javascript-obfuscator `这个库：

```js
npm install javascript-obfuscator -g
```

安装完成后，`javascript-obfuscator`就是一个独立的可执行命令了。



##### 2.3.1 **代码压缩**

这里` javascript-obfuscator `也提供了代码压缩的功能，使用其参数 `compact `即可完成` JavaScript` 代码的压缩，输出为一行内容。默认是 true，如果定义为 false，则混淆后的代码会分行显示。

```js
var code = `
let x = '1' + 1
console.log('x', x)
	`

const options = {
  compact: true,  // 代码压缩配置
}

const obfuscator = require('javascript-obfuscator')

function obfuscate(code, options) {
  return obfuscator.obfuscate(code, options).getObfuscatedCode()
}

console.log(obfuscate(code, options))
```

##### 2.3.2 **变量名混淆**

变量名混淆可以通过配置` identifierNamesGenerator` 参数实现，我们通过这个参数可以控制变量名混淆的方式，如` hexadecimal `则会替换为 16 进制形式的字符串，在这里我们可以设定如下值：

+ `hexadecimal`：将变量名替换为 16 进制形式的字符串，如 `0xabc123`。
+ `mangled`：将变量名替换为普通的简写字符，如 a、b、c 等。
  该参数默认为` hexadecimal`。

我们将该参数修改为 `mangled` 来试一下：

```js
const code = `
let hello = '1' + 1
console.log('hello', hello)
`
const options = {
  compact: true,
  identifierNamesGenerator: 'mangled'
}
```

##### 2.3.3 字符串混淆

字符串混淆，即将一个字符串声明放到一个数组里面，使之无法被直接搜索到。我们可以通过控制 `stringArray` 参数来控制，默认为 true。

```js
const code = `
var a = 'hello world'
`;
const options = {
  compact: false,
  unicodeEscapeSequence: true  //对字符串进行 Unicode 转码
};
```



### 3 混淆突破1

#### 3.1 逆向目标

+ 首页：https://www.kaogujia.com/

+ API：https://service.kaogujia.com/api/sku/search
+ 参数：result:`DqpF5ZqkLKav2qDLkaNP1F9fq`

#### 3.2 逆向分析

+ 经过分析，这里面有一个`.then`方法

![image-20220822161102652](images\image-20220822161102652.png)

+ 查看响应的数据，发现这个地方获取返回的数据，会做解密处理

  ![image-20220822161747333](images\image-20220822161747333.png)

+ 定位响应的结果，可以发现这里是数据进行转码

  ![image-20220822162112918](images\image-20220822162112918.png)



+ `_0xe980c9['d']` 这是一个接密函数，对数据进行解密。

  ![image-20220822162230800](images\image-20220822162230800.png)



#### 3.3 逆向结果

```javascript
var _0x19a136 = require('crypto-js');

  a0_0x2d46 = function(_0x2d4608, _0x56d9a3) {
        _0x2d4608 = _0x2d4608 - 0x170;
        var _0xfdbc8a = _0x32d16e[_0x2d4608];
        return _0xfdbc8a;
    }
      function _0x1ee15c(_0xf38f80) {
            var _0x25ef49 = encodeURI(_0xf38f80)
              , _0x3b0495 = btoa(_0x25ef49);
            return _0x3b0495;
        }

_0xf0f326 = function(_0x2cd9c5, _0x1f4c48) {
            var _0x258721 = a0_0x2d46;
            if ('string' === typeof _0x2cd9c5) {
                var _0x53a751 = _0x1ee15c(_0x2cd9c5)['repeat'](0x3)
                  , _0x1426a5 = _0x53a751['slice'](0x0, 0x10)
                  , _0x9e79e2 = _0x53a751['slice'](0xc, 0x1c)
                  , _0x3aabdc = _0x19a136['enc']['Utf8']['parse'](_0x1426a5)
                  , _0x5b6fc0 = _0x19a136['enc']['Utf8']['parse'](_0x9e79e2)
                  , _0x1f587d = _0x19a136['AES']['decrypt'](_0x1f4c48, _0x3aabdc, {
                    'iv': _0x5b6fc0,
                    'mode': _0x19a136['mode']['CBC'],
                    'padding': _0x19a136['pad']['Pkcs7']
                });
                return _0x1f587d['toString'](_0x19a136['enc']['Utf8']);
            }
        };
```

![image-20220822162733868](images\image-20220822162733868.png)



### 4 混淆突破2

#### 4.1 逆向目标

+ 首页：https://bz.zzzmh.cn/index
+ API：https://api.zzzmh.cn/bz/v3/getData

+ 目标：result: `ak+9VCsq4dEdB+UdVfGo8kh5JDEbMHGTCmF/`

#### 4.2 逆向分析

+ 解除无限debugger

  ```javascript
  Function.prototype.__constructor_back = Function.prototype.constructor;
  Function.prototype.constructor = function() {
      if(arguments && typeof arguments[0]==='string'){
          if("debugger" === arguments[0]){
              return
          }
      }
     return Function.prototype.__constructor_back.apply(this,arguments);
  }
  ```

+ 下`xhr`断点调试，跟栈调试

![image-20220822164135259](images\image-20220822164135259.png)

+ 解密方法

  ```javascript
  _0x3042ee['a']['decipher'](_0x45e4b9['data'][_0x4a9a('0x67', 'uMwG')])
  ```

##### 4.2.1 找到执行解密函数的位置

![image-20220823143310893](images\image-20220823143310893.png)

注:可以看到这里是使用相关函数对该代码进行了解密操作，找对对应的函数模拟相关操作即可

#### 4.3 逆向结果

+ 替换混淆的关键字，输出对应的结果。

```javascript
   function _0x278324(_0x12a8a9) {
                for (var _0x3e43f6, _0x506ac2, _0x7f0f4 = '', _0x2150c4 = 0x0; _0x2150c4 < _0x12a8a9['length']; )
                    _0x3e43f6 = _0x12a8a9[_0x2150c4],
                    _0x506ac2 = 0x0,
                    _0x3e43f6 >>> 0x7 === 0x0 ? (_0x7f0f4 += String['fromCharCode'](_0x12a8a9[_0x2150c4]),
                    _0x2150c4 += 0x1) : 0xfc === (0xfc & _0x3e43f6) ? (_0x506ac2 = (0x3 & _0x12a8a9[_0x2150c4]) << 0x1e,
                    _0x506ac2 |= (0x3f & _0x12a8a9[_0x2150c4 + 0x1]) << 0x18,
                    _0x506ac2 |= (0x3f & _0x12a8a9[_0x2150c4 + 0x2]) << 0x12,
                    _0x506ac2 |= (0x3f & _0x12a8a9[_0x2150c4 + 0x3]) << 0xc,
                    _0x506ac2 |= (0x3f & _0x12a8a9[_0x2150c4 + 0x4]) << 0x6,
                    _0x506ac2 |= 0x3f & _0x12a8a9[_0x2150c4 + 0x5],
                    _0x7f0f4 += String['fromCharCode'](_0x506ac2),
                    _0x2150c4 += 0x6) : 0xf8 === (0xf8 & _0x3e43f6) ? (_0x506ac2 = (0x7 & _0x12a8a9[_0x2150c4]) << 0x18,
                    _0x506ac2 |= (0x3f & _0x12a8a9[_0x2150c4 + 0x1]) << 0x12,
                    _0x506ac2 |= (0x3f & _0x12a8a9[_0x2150c4 + 0x2]) << 0xc,
                    _0x506ac2 |= (0x3f & _0x12a8a9[_0x2150c4 + 0x3]) << 0x6,
                    _0x506ac2 |= 0x3f & _0x12a8a9[_0x2150c4 + 0x4],
                    _0x7f0f4 += String['fromCharCode'](_0x506ac2),
                    _0x2150c4 += 0x5) : 0xf0 === (0xf0 & _0x3e43f6) ? (_0x506ac2 = (0xf & _0x12a8a9[_0x2150c4]) << 0x12,
                    _0x506ac2 |= (0x3f & _0x12a8a9[_0x2150c4 + 0x1]) << 0xc,
                    _0x506ac2 |= (0x3f & _0x12a8a9[_0x2150c4 + 0x2]) << 0x6,
                    _0x506ac2 |= 0x3f & _0x12a8a9[_0x2150c4 + 0x3],
                    _0x7f0f4 += String['fromCharCode'](_0x506ac2),
                    _0x2150c4 += 0x4) : 0xe0 === (0xe0 & _0x3e43f6) ? (_0x506ac2 = (0x1f & _0x12a8a9[_0x2150c4]) << 0xc,
                    _0x506ac2 |= (0x3f & _0x12a8a9[_0x2150c4 + 0x1]) << 0x6,
                    _0x506ac2 |= 0x3f & _0x12a8a9[_0x2150c4 + 0x2],
                    _0x7f0f4 += String['fromCharCode'](_0x506ac2),
                    _0x2150c4 += 0x3) : 0xc0 === (0xc0 & _0x3e43f6) ? (_0x506ac2 = (0x3f & _0x12a8a9[_0x2150c4]) << 0x6,
                    _0x506ac2 |= 0x3f & _0x12a8a9[_0x2150c4 + 0x1],
                    _0x7f0f4 += String['fromCharCode'](_0x506ac2),
                    _0x2150c4 += 0x2) : (_0x7f0f4 += String['fromCharCode'](_0x12a8a9[_0x2150c4]),
                    _0x2150c4 += 0x1);
                return _0x7f0f4;
            }

   function _0x5ac2c2(_0x12a8a9) {
                for (var _0x3e43f6 = [-0x6f, 0x34, 0x5b, 0x41, -0x41, 0x74, 0x77, 0x6a, -0x79, -0x52, -0x5, 0x50, 0x33, 0x61, 0x44, -0x53, -0x70, -0x33, 0x17, -0x2e, -0x22, -0x72, -0x37, -0xb, -0x7f, 0x5a, 0x21, 0x16, -0x1f, 0x32, -0x11, 0x14, -0x2c, 0xf, -0x5e, -0x7b, 0x76, -0x17, -0x3d, 0x72, 0x47, -0x68, -0x7e, -0x75, -0x51, -0x36, -0x12, -0x6e, -0x4, -0x5f, -0x5b, 0x5e, -0x50, -0xe, 0x78, 0x69, 0x55, 0x68, -0x56, -0x6c, 0x43, 0x19, 0x65, 0x6c, 0x10, -0x69, 0x6f, -0xa, 0x75, -0x49, 0x4d, 0x59, -0x1d, -0x62, -0x44, 0x70, 0x6b, -0x1, 0x56, 0x79, 0x58, -0x65, -0x7c, 0x45, -0x1e, -0x8, -0x71, -0x4a, -0x76, 0x39, -0x19, 0xc, -0x73, -0x6a, 0x5f, 0x7f, 0x54, 0x7c, -0x66, -0x1c, 0x49, 0x2b, -0x3c, 0x1c, 0x2e, 0x73, 0x1e, 0x7a, -0x4b, 0x7d, -0x43, -0x4d, 0x3, -0x7, -0x35, -0xd, 0x35, 0x4e, -0x48, 0x1, 0xb, -0x47, -0x27, -0x4f, -0x3, 0x13, 0x29, 0x7e, -0x2b, -0x7d, -0x1b, 0x22, 0x3f, 0x8, 0x48, -0x23, -0x29, -0x3f, 0x3c, -0x18, 0x66, 0x2f, -0x77, -0x67, -0x16, 0x2d, 0x3b, 0x40, -0x60, 0x31, 0x53, -0x6b, -0x78, -0x39, -0x46, 0x0, -0x26, -0x54, -0x28, 0x18, 0xe, 0x30, 0x1d, 0x2c, -0x24, -0x2f, 0x38, -0x5c, 0x26, 0x25, 0x4, -0x32, 0x67, 0xa, -0x59, 0x37, 0x71, -0x1a, 0x6e, 0x36, 0x24, -0x14, -0x4e, -0xc, -0x74, 0x46, -0x25, 0x5, -0x3e, -0x4c, -0x30, -0x40, 0x4f, 0x64, 0x28, 0x6, -0x3a, -0x5a, -0x13, -0x9, 0x27, 0x5d, -0x63, 0x15, 0x7, 0x1a, -0x2, 0x1b, -0x2d, 0x51, 0x3a, -0x7a, 0x4c, -0x42, 0x2, 0x5c, -0x2a, 0x62, -0x10, 0x9, 0x3d, 0x3e, -0xf, 0x63, -0x15, 0x1f, -0x38, 0x57, 0x11, -0x34, -0x45, -0x21, -0x3b, -0x55, 0x42, 0x4a, 0x12, -0x5d, -0x80, -0x57, -0x20, 0x2a, 0x20, -0x58, 0x6d, 0x60, 0xd, -0x6, 0x4b, -0x64, -0x31, 0x23, -0x61, 0x52, -0x6d, 0x7b], _0x506ac2 = 0x0, _0x7f0f4 = 0x0, _0x2150c4 = 0x0, _0x86d2ea = new Array(), _0x2fb28c = 0x0; _0x2fb28c < _0x12a8a9['length']; _0x2fb28c++) {
                    _0x506ac2 = _0x506ac2 + 0x1 & 0xff,
                    _0x7f0f4 = (0xff & _0x3e43f6[_0x506ac2]) + _0x7f0f4 & 0xff;
                    var _0x5ac2c2 = _0x3e43f6[_0x506ac2];
                    _0x3e43f6[_0x506ac2] = _0x3e43f6[_0x7f0f4],
                    _0x3e43f6[_0x7f0f4] = _0x5ac2c2,
                    _0x2150c4 = (0xff & _0x3e43f6[_0x506ac2]) + (0xff & _0x3e43f6[_0x7f0f4]) & 0xff,
                    _0x86d2ea['push'](_0x12a8a9[_0x2fb28c] ^ _0x3e43f6[_0x2150c4]);
                }
                return _0x86d2ea;
            }

   function _0x3ac9f9(_0x12a8a9) {
            for (var _0x3e43f6 = atob(_0x12a8a9), _0x506ac2 = new Int8Array(_0x3e43f6['length']), _0x7f0f4 = 0x0; _0x7f0f4 < _0x3e43f6['length']; _0x7f0f4++)
                _0x506ac2[_0x7f0f4] = _0x3e43f6['charCodeAt'](_0x7f0f4);
            return _0x506ac2;
        }

 function _0xc0d35b(_0x12a8a9) {
        return _0x278324(_0x5ac2c2(_0x3ac9f9(_0x12a8a9)));
    }
```



**数据结果展示**

![image-20220823144953793](images\image-20220823144953793.png)





###  5 octet-stream

简介：**octet**-**stream指任意类型的二进制流数据。**



#### 1 逆向目标

+ 地址：http://www.spolicy.com/
+ 接口：http://www.spolicy.com/info_api/policyType/showPolicyType
+ 目标：参数加密

#### 2 逆向分析

下xhr断点,开始分析，往下执行可以发现数据接收有一个响应拦截器

![image-20221127160137806](images\image-20221127160137806.png)



可以从这个位置找请求拦截器进行分析，定位以后，先从请求拦截器里面分析代码，看明文到密文的切换经过了什么操作。

![image-20221127160313986](images\image-20221127160313986.png)



此图为明文数据

![image-20221127160431906](images\image-20221127160431906.png)

往下看代码和业务逻辑，27233是数据的加密位置，他是从明文到密文的转换

![image-20221127160758958](images\image-20221127160758958.png)

跟到内部的核心代码查看，数据是进入这个方法里面加密的

![image-20221127160928964](images\image-20221127160928964.png)









