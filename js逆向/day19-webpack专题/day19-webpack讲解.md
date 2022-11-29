## `WebPack`打包

`webpack`是一个基于模块化的打包（构建）工具, 它把一切都视作模块

**概念：**

​       `webpack`是 `JavaScript` 应用程序的模块打包器,可以把开发中的所有资源（图片、js文件、css文件等）都看成模块，通过loader（加载器）和`plugins`（插件）对资源进行处理，打包成符合生产环境部署的前端资源。所有的资源都是通过`JavaScript`渲染出来的。



如果一个页面大部分是script标签构成，80%以上是`webpack`打包。

**地址**：http://cls.cn/telegraph

![img](https://app.yinxiang.com/FileSharing.action?hash=1/7d9dde72b8262d871a27f10af50a9b44-286201)



### 1. `webpack`打包简介

![img](https://app.yinxiang.com/FileSharing.action?hash=1/62be23ee03da0e043ff4b088eb0872cd-72813)



![image-20220329153518062](./images\image-20220329153518062.png)



#### 1.0 多个`JS`文件打包：

​		如果模块比较多，就会将模块打包成JS文件, 然后定义一个全局变量 window["webpackJsonp"] = [ ]，它的作用是存储需要动态导入的模块，然后重写 window["webpackJsonp"] 数组的 push( ) 方法为 webpackJsonpCallback( ),也就是说 window["webpackJsonp"].push( ) 其实执行的是 webpackJsonpCallback( ),window["webpackJsonp"].push( )接收三个参数,第一个参数是模块的ID,第二个参数是 一个数组或者对象,里面定义大量的函数,第三个参数是要调用的函数(可选)

![img](https://app.yinxiang.com/FileSharing.action?hash=1/46d51af6b6946548adccc97f31a249ef-20029)



#### 1.1 `webpack`数组形式

+ 给需要处理业务的模块进行打包，通过下标取值。

```javascript
!function(e) {
    var t = {};

    // 加载器  所有的模块都是从这个函数加载 执行
    function n(r) {
        if (t[r])
            return t[r].exports;
        var o = t[r] = {
            i: r,
            l: !1,
            exports: {}
        };
        return e[r].call(o.exports, o, o.exports, n),
            o.l = !0,
            o.exports
    }

    n(0)
}
    ([
        function () {
            console.log('123456')
        },

              function () {
            console.log('模块2')
        },
    ])
```

#### 1.2 `webpack`对象形式

+ 给需要处理业务的模块进行打包，通过`key`取值。

```javascript
!function(e) {
    var t = {};
    //  所有的模块 都是从这个加载器 执行的  分发器
    function n(r) {
        if (t[r])
            return t[r].exports;
        var o = t[r] = {
            i: r,
            l: !1,
            exports: {}
        };
        return e[r].call(o.exports, o, o.exports, n),
        o.l = !0,
        o.exports
    }
   n('xialuo')  // 对象 根据KEY 找模块
}({

        0: function () {
            console.log('我是模块1  负责加密')
        },

        'xialuo': function () {
            console.log('我是模块2  负责解密')
        },

        2: function () {
            console.log('我是模块3  负责爬数据')
        }
    }
);
```



### 2. `webpack`教学

#### 2.1 逆向目标

+ 首页：https://agent.leju.com/ucenter/passportlogin/

+ 接口：https://agent.leju.com/ucenter/login/

+ 逆向参数：`password: 8cbf7f88e70300def68533a74c77b785e11d743c77627b624`

#### 2.2 逆向分析

+ 全局搜索`password`参数，然后下断点调试，可以发现加密逻辑在`loginNew_9697dc1c616207641ca0.js`里面。



![image-20220821172434242](images\image-20220821172434242.png)

+ 点击进去，发现是模块

  ![image-20220821173358041](images\image-20220821173358041.png)



+ 导出加载器，查看所有模块

![image-20220821180249172](images\image-20220821180249172.png)

#### 2.3 代码处理

+ 找出对应负责模块

![image-20220821181840088](images\image-20220821181840088.png)



```javascript


var _xx;
!function(t) {
    var e = {};
    function i(n) {
        if (e[n])
            return e[n].exports;
        var s = e[n] = {
            i: n,
            l: !1,
            exports: {}
        };
        console.log(n)
        return t[n].call(s.exports, s, s.exports, i),
        s.l = !0,
        s.exports
    }
    i.m = t,
    i.c = e,
    i.d = function(t, e, n) {
        i.o(t, e) || Object.defineProperty(t, e, {
            enumerable: !0,
            get: n
        })
    }
    ,
    i.r = function(t) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(t, "__esModule", {
            value: !0
        })
    }
    ,
    i.t = function(t, e) {
        if (1 & e && (t = i(t)),
        8 & e)
            return t;
        if (4 & e && "object" == typeof t && t && t.__esModule)
            return t;
        var n = Object.create(null);
        if (i.r(n),
        Object.defineProperty(n, "default", {
            enumerable: !0,
            value: t
        }),
        2 & e && "string" != typeof t)
            for (var s in t)
                i.d(n, s, function(e) {
                    return t[e]
                }
                .bind(null, s));
        return n
    }
    ,
    i.n = function(t) {
        var e = t && t.__esModule ? function() {
            return t.default
        }
        : function() {
            return t
        }
        ;
        return i.d(e, "a", e),
        e
    }
    ,
    i.o = function(t, e) {
        return Object.prototype.hasOwnProperty.call(t, e)
    }
    ,
    i.p = "//esfres.leju.com/agent_www_new/dist/",
    // i(i.s = 301)
       _xx = i;

}({
 305: function(t, e, i) {
        "use strict";
        Object.defineProperty(e, "__esModule", {
            value: !0
        }),
        e.encryptedString = e.RSAKeyPair = void 0;
        var n = i(228)
          , s = i(306)
          , o = {};
        o.NoPadding = "NoPadding",
        o.PKCS1Padding = "PKCS1Padding",
        o.RawEncoding = "RawEncoding",
        o.NumericEncoding = "NumericEncoding",
        e.RSAKeyPair = function(t, e, i, o) {
            this.e = (0,
            n.biFromHex)(t),
            this.d = (0,
            n.biFromHex)(e),
            this.m = (0,
            n.biFromHex)(i),
            this.chunkSize = "number" != typeof o ? 2 * (0,
            n.biHighIndex)(this.m) : o / 8,
            this.radix = 16,
            this.barrett = new s.BarrettMu(this.m)
        }
        ,
        e.encryptedString = function(t, e, i, s) {
            var a, r, l, c, u, d, p, h, f, g = new Array, m = e.length, y = "";
            for (c = "string" == typeof i ? i == o.NoPadding ? 1 : i == o.PKCS1Padding ? 2 : 0 : 0,
            u = "string" == typeof s && s == o.RawEncoding ? 1 : 0,
            1 == c ? m > t.chunkSize && (m = t.chunkSize) : 2 == c && m > t.chunkSize - 11 && (m = t.chunkSize - 11),
            a = 0,
            r = 2 == c ? m - 1 : t.chunkSize - 1; a < m; )
                c ? g[r] = e.charCodeAt(a) : g[a] = e.charCodeAt(a),
                a++,
                r--;
            for (1 == c && (a = 0),
            r = t.chunkSize - m % t.chunkSize; r > 0; ) {
                if (2 == c) {
                    for (d = Math.floor(256 * Math.random()); !d; )
                        d = Math.floor(256 * Math.random());
                    g[a] = d
                } else
                    g[a] = 0;
                a++,
                r--
            }
            for (2 == c && (g[m] = 0,
            g[t.chunkSize - 2] = 2,
            g[t.chunkSize - 1] = 0),
            p = g.length,
            a = 0; a < p; a += t.chunkSize) {
                for (h = new n.BigInt,
                r = 0,
                l = a; l < a + t.chunkSize; ++r)
                    h.digits[r] = g[l++],
                    h.digits[r] += g[l++] << 8;
                f = t.barrett.powMod(h, t.e),
                y += 1 == u ? biToBytes(f) : 16 == t.radix ? (0,
                n.biToHex)(f) : biToString(f, t.radix)
            }
            return y
        }
    },
           228: function(t, e, i) {
        "use strict";
        Object.defineProperty(e, "__esModule", {
            value: !0
        });
        var n, s;
        function o(t) {
n = new Array(t);
            for (var e = 0; e < n.length; e++)
                n[e] = 0;
            new a,
            (s = new a).digits[0] = 1
        }
        o(20);
        l(1e15);
        function a(t) {
            this.digits = "boolean" == typeof t && 1 == t ? null : n.slice(0),
            this.isNeg = !1
        }
        function r(t) {
            var e = new a(!0);
            return e.digits = t.digits.slice(0),
            e.isNeg = t.isNeg,
            e
        }
        function l(t) {
            var e = new a;
            e.isNeg = t < 0,
            t = Math.abs(t);
            for (var i = 0; t > 0; )
                e.digits[i++] = 65535 & t,
                t >>= 16;
            return e
        }
        function c(t) {
            for (var e = "", i = t.length - 1; i > -1; --i)
                e += t.charAt(i);
            return e
        }
        new Array("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z");
        var u = new Array("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f");
        function d(t) {
            for (var e = "", i = 0; i < 4; ++i)
                e += u[15 & t],
                t >>>= 4;
            return c(e)
        }
        function p(t) {
            return t >= 48 && t <= 57 ? t - 48 : t >= 65 && t <= 90 ? 10 + t - 65 : t >= 97 && t <= 122 ? 10 + t - 97 : 0
        }
        function h(t) {
            for (var e = 0, i = Math.min(t.length, 4), n = 0; n < i; ++n)
                e <<= 4,
                e |= p(t.charCodeAt(n));
            return e
        }
        function f(t, e) {
            var i;
            if (t.isNeg != e.isNeg)
                e.isNeg = !e.isNeg,
                i = g(t, e),
                e.isNeg = !e.isNeg;
            else {
                i = new a;
                for (var n, s = 0, o = 0; o < t.digits.length; ++o)
                    n = t.digits[o] + e.digits[o] + s,
                    i.digits[o] = 65535 & n,
                    s = Number(n >= 65536);
                i.isNeg = t.isNeg
            }
            return i
        }
        function g(t, e) {
            var i;
            if (t.isNeg != e.isNeg)
                e.isNeg = !e.isNeg,
                i = f(t, e),
                e.isNeg = !e.isNeg;
            else {
                var n, s;
                i = new a,
                s = 0;
                for (var o = 0; o < t.digits.length; ++o)
                    n = t.digits[o] - e.digits[o] + s,
                    i.digits[o] = 65535 & n,
                    i.digits[o] < 0 && (i.digits[o] += 65536),
                    s = 0 - Number(n < 0);
                if (-1 == s) {
                    s = 0;
                    for (o = 0; o < t.digits.length; ++o)
                        n = 0 - i.digits[o] + s,
                        i.digits[o] = 65535 & n,
                        i.digits[o] < 0 && (i.digits[o] += 65536),
                        s = 0 - Number(n < 0);
                    i.isNeg = !t.isNeg
                } else
                    i.isNeg = t.isNeg
            }
            return i
        }
        function m(t) {
            for (var e = t.digits.length - 1; e > 0 && 0 == t.digits[e]; )
                --e;
            return e
        }
        function y(t) {
            var e, i = m(t), n = t.digits[i], s = 16 * (i + 1);
            for (e = s; e > s - 16 && 0 == (32768 & n); --e)
                n <<= 1;
            return e
        }
        function v(t, e) {
            for (var i, n, s, o = new a, r = m(t), l = m(e), c = 0; c <= l; ++c) {
                i = 0,
                s = c;
                for (var u = 0; u <= r; ++u,
                ++s)
                    n = o.digits[s] + t.digits[u] * e.digits[c] + i,
                    o.digits[s] = 65535 & n,
                    i = n >>> 16;
                o.digits[c + r + 1] = i
            }
            return o.isNeg = t.isNeg != e.isNeg,
            o
        }
        function b(t, e) {
            var i, n, s, o = new a;
            i = m(t),
            n = 0;
            for (var r = 0; r <= i; ++r)
                s = o.digits[r] + t.digits[r] * e + n,
                o.digits[r] = 65535 & s,
                n = s >>> 16;
            return o.digits[1 + i] = n,
            o
        }
        function w(t, e, i, n, s) {
            for (var o = Math.min(e + s, t.length), a = e, r = n; a < o; ++a,
            ++r)
                i[r] = t[a]
        }
        var k = new Array(0,32768,49152,57344,61440,63488,64512,65024,65280,65408,65472,65504,65520,65528,65532,65534,65535);
        function C(t, e) {
            var i = Math.floor(e / 16)
              , n = new a;
            w(t.digits, 0, n.digits, i, n.digits.length - i);
            for (var s = e % 16, o = 16 - s, r = n.digits.length - 1, l = r - 1; r > 0; --r,
            --l)
                n.digits[r] = n.digits[r] << s & 65535 | (n.digits[l] & k[s]) >>> o;
            return n.digits[0] = n.digits[r] << s & 65535,
            n.isNeg = t.isNeg,
            n
        }
        var x = new Array(0,1,3,7,15,31,63,127,255,511,1023,2047,4095,8191,16383,32767,65535);
        function _(t, e) {
            var i = Math.floor(e / 16)
              , n = new a;
            w(t.digits, i, n.digits, 0, t.digits.length - i);
            for (var s = e % 16, o = 16 - s, r = 0, l = r + 1; r < n.digits.length - 1; ++r,
            ++l)
                n.digits[r] = n.digits[r] >>> s | (n.digits[l] & x[s]) << o;
            return n.digits[n.digits.length - 1] >>>= s,
            n.isNeg = t.isNeg,
            n
        }
        function $(t, e) {
            var i = new a;
            return w(t.digits, 0, i.digits, e, i.digits.length - e),
            i
        }
        function S(t, e) {
            if (t.isNeg != e.isNeg)
                return 1 - 2 * Number(t.isNeg);
            for (var i = t.digits.length - 1; i >= 0; --i)
                if (t.digits[i] != e.digits[i])
                    return t.isNeg ? 1 - 2 * Number(t.digits[i] > e.digits[i]) : 1 - 2 * Number(t.digits[i] < e.digits[i]);
            return 0
        }
        function j(t, e) {
            var i, n, o = y(t), l = y(e), c = e.isNeg;
            if (o < l)
                return t.isNeg ? ((i = r(s)).isNeg = !e.isNeg,
                t.isNeg = !1,
                e.isNeg = !1,
                n = g(e, t),
                t.isNeg = !0,
                e.isNeg = c) : (i = new a,
                n = r(t)),
                new Array(i,n);
            i = new a,
            n = t;
            for (var u = Math.ceil(l / 16) - 1, d = 0; e.digits[u] < 32768; )
                e = C(e, 1),
                ++d,
                ++l,
                u = Math.ceil(l / 16) - 1;
            n = C(n, d),
            o += d;
            for (var p = Math.ceil(o / 16) - 1, h = $(e, p - u); -1 != S(n, h); )
                ++i.digits[p - u],
                n = g(n, h);
            for (var v = p; v > u; --v) {
                var w = v >= n.digits.length ? 0 : n.digits[v]
                  , k = v - 1 >= n.digits.length ? 0 : n.digits[v - 1]
                  , x = v - 2 >= n.digits.length ? 0 : n.digits[v - 2]
                  , j = u >= e.digits.length ? 0 : e.digits[u]
                  , A = u - 1 >= e.digits.length ? 0 : e.digits[u - 1];
                i.digits[v - u - 1] = w == j ? 65535 : Math.floor((65536 * w + k) / j);
                for (var T = i.digits[v - u - 1] * (65536 * j + A), q = 4294967296 * w + (65536 * k + x); T > q; )
                    --i.digits[v - u - 1],
                    T = i.digits[v - u - 1] * (65536 * j | A),
                    q = 65536 * w * 65536 + (65536 * k + x);
                (n = g(n, b(h = $(e, v - u - 1), i.digits[v - u - 1]))).isNeg && (n = f(n, h),
                --i.digits[v - u - 1])
            }
            return n = _(n, d),
            i.isNeg = t.isNeg != c,
            t.isNeg && (i = c ? f(i, s) : g(i, s),
            n = g(e = _(e, d), n)),
            0 == n.digits[0] && 0 == m(n) && (n.isNeg = !1),
            new Array(i,n)
        }
        e.setMaxDigits = o,
        e.biFromHex = function(t) {
            for (var e = new a, i = t.length, n = 0; i > 0; i -= 4,
            ++n)
                e.digits[n] = h(t.substr(Math.max(i - 4, 0), Math.min(i, 4)));
            return e
        }
        ,
        e.biHighIndex = m,
        e.biCopy = r,
        e.BigInt = a,
        e.biDivide = function(t, e) {
            return j(t, e)[0]
        }
        ,
        e.biMultiply = v,
        e.biDivideByRadixPower = function(t, e) {
            var i = new a;
            return w(t.digits, e, i.digits, 0, i.digits.length - e),
            i
        }
        ,
        e.biModuloByRadixPower = function(t, e) {
            var i = new a;
            return w(t.digits, 0, i.digits, 0, e),
            i
        }
        ,
        e.biSubtract = g,
        e.biCompare = S,
        e.biShiftRight = _,
        e.biToHex = function(t) {
            for (var e = "", i = (m(t),
            m(t)); i > -1; --i)
                e += d(t.digits[i]);
            return e
        }
    },
        306: function(t, e, i) {
        "use strict";
        Object.defineProperty(e, "__esModule", {
            value: !0
        }),
        e.BarrettMu_powMod = e.BarrettMu_multiplyMod = e.BarrettMu_modulo = e.BarrettMu = void 0;
        var n = i(228);
        function s(t) {
            var e = (0,
            n.biDivideByRadixPower)(t, this.k - 1)
              , i = (0,
            n.biMultiply)(e, this.mu)
              , s = (0,
            n.biDivideByRadixPower)(i, this.k + 1)
              , o = (0,
            n.biModuloByRadixPower)(t, this.k + 1)
              , a = (0,
            n.biMultiply)(s, this.modulus)
              , r = (0,
            n.biModuloByRadixPower)(a, this.k + 1)
              , l = (0,
            n.biSubtract)(o, r);
            l.isNeg && (l = biAdd(l, this.bkplus1));
            for (var c = (0,
            n.biCompare)(l, this.modulus) >= 0; c; )
                l = (0,
                n.biSubtract)(l, this.modulus),
                c = (0,
                n.biCompare)(l, this.modulus) >= 0;
            return l
        }
        function o(t, e) {
            var i = (0,
            n.biMultiply)(t, e);
            return this.modulo(i)
        }
        function a(t, e) {
            var i = new n.BigInt;
            i.digits[0] = 1;
            for (var s = t, o = e; 0 != (1 & o.digits[0]) && (i = this.multiplyMod(i, s)),
            0 != (o = (0,
            n.biShiftRight)(o, 1)).digits[0] || 0 != (0,
            n.biHighIndex)(o); )
                s = this.multiplyMod(s, s);
            return i
        }
        e.BarrettMu = function(t) {
            this.modulus = (0,
            n.biCopy)(t),
            this.k = (0,
            n.biHighIndex)(this.modulus) + 1;
            var e = new n.BigInt;
            e.digits[2 * this.k] = 1,
            this.mu = (0,
            n.biDivide)(e, this.modulus),
            this.bkplus1 = new n.BigInt,
            this.bkplus1.digits[this.k + 1] = 1,
            this.modulo = s,
            this.multiplyMod = o,
            this.powMod = a
        }
        ,
        e.BarrettMu_modulo = s,
        e.BarrettMu_multiplyMod = o,
        e.BarrettMu_powMod = a
    }
})

console.log(_xx(305))

function get_pwd(pwd){
        var a = _xx(228);
     (0, a.setMaxDigits) (129);
    var r = _xx(305);
   var n = new r.RSAKeyPair("10001","","BC087C7C00848CE8A349C9072C3229E0D595F817EDDE9ABF6FC72B41942A759E97956CE9CB7D1F2E99399EADBACC0531F16EAE8EFCB68553DE0E125B2231ED955ADBF5208E65DC804237C93EB23C83E7ECDA0B586ECF31839038EE6B640E0EEC5FF17D219FDEA33E730F287F0D384C74A53DFE1F91ACC63C7C92039A43AC6E97");
   var s = (0, r.encryptedString)(n, pwd);
     return s
}

console.log(get_pwd('123456'));
```





### 3. `webpack`教学

#### 3.1 逆向目标

+ 地址：https://static.waitwaitpay.com/web/sd_se/index.html
+ 接口：https://api.waitwaitpay.com/api/vendors/nearby
+ 目标：响应数据`ZmQzOTI0MjBlNnic7VvJcuM4Ev0aHqXADuRRtKWIPnT0uU8KEABtdWkbLVXj`

#### 3.2 逆向分析



打开目标网站，往下拉，在开发者工具可以抓到这三个包，其中nearby接口请求到的数据是加密之后的密文



![image-20220329140603995](./images\image-20220329140603995.png)



##### 3.2.1 关键字搜索 

这个时候可以尝试再在该文件里搜索 JSON.parse( ，就会找到这样一个地方，这里可以发现有一个decode函数，就比较可疑，下个断点

![image-20220329141945204](images\image-20220329141945204.png)

**数据处理**

往上看堆栈，可以发现该函数就是解密的入口，讲请求得到的加密数据e传到f函数，即可解密得到明文数据

![image-20220329142942404](images\image-20220329142942404.png)





可以很明显的看到这个f函数内部关键调用了这两个函数来进行数据的解密，那么，我们首先就来看看这个 a.default.decode ，向上寻找a是在哪里被定义的



![image-20220329150156127](images\image-20220329150156127.png)

可发现 a = s(n(432))，这里的432就是代表导出webpack打包的大数组里面第432个大函数，大数组指的是这个大数组

##### 3.2.2 JavaScript分析

​		那我们在本地js里面，怎么才能实现像浏览器这样导出呢，这个时候我们可以直接去找到 **导出器** 类似于 **exports** 这样的关键字，所有的 **webpack** 导出器都是长这样的

![image-20220329150257570](images\image-20220329150257570.png)



+ 直接复制全部的代码，之前已经发现处理解密的话只有`f`函数，观察整个函数调用第三方库很少，那么就可以全复制代码，然后调用这个函数即可。

+ 直接扣出加密代码，调用当前这个函数

  + 本地的话，我们就可以这样来进行导出然后赋值给a还有o

    ```javascript
    function s(e) {
        return e && e.__esModule ? e : {
            default: e
        }
    };
    // 这里的window.xiaoxiaobai就是上面导出器函数
    var a = s(window.xl(432));
    var o = s(window.xl(423));
    ```

    ![image-20220821214608114](images\image-20220821214608114.png)

#### 3.3 代码处理

+ 代码比较多。6w多行！！就不复制在这儿了，有需要的上百度网盘下载

```
链接：https://pan.baidu.com/s/1bkTFBs0oehozi32b6btaqQ 
提取码：m57l
```



### 总结

+ 找到这个加载器
+ 找到调用模块
+ 构造一个自执行方法
+ 导出加密方法
+ 编写自定义方法 按照流程加密







