## javascript调试

**学习收获**

+ 浏览器的基本使用
+ 浏览器调试断点讲解
+ 怎么过无限debugger
+ hook调试奇门技巧
+ 常见补环境方法



### 1. 浏览器面板补充

#### Elements

#### Network

+ 保留日志
  + 勾选每次刷新不会清除之前的请求
+ 停用缓存
  + 勾选后不会从缓存里面拉数据，方便后续JS动态调试

#### Sources

+ page ： 所有资源文件

+ filesystem： 关联本地文件

+ overrides：  可以做文件替换，比如替换JS

+ 代码段：可以编写脚本，影响页面,代码记录

  + ```javascript
    var a =document.querySelector("#su")
    // 可以在控制台操作 输入 a.remove()
    ```

+ 断点介绍

  地址：https://oauth.d.cn/auth/goLogin.html

  + 跳过子函数（次态函数）执行（只在主函数内一步一步执行，不进入子函数内部）
  + 进入子函数（次态函数）执行（在主函数内部一步一步执行，如果遇到子函数，会跳转到子函数内部一步一步执行）
  + 跳出当前函数，回到调用位置
  + 单步执行，会进入到函数内部 更加的细致
  + 屏蔽断点

#### Application

+ 

### 3 断点讲解

**作用：**对数据进行监听，跟值进行分析

#### 3.1 什么是断点

**网站运行时间轴**

```
加载Hmtl - 加载JS - 运行JS初始化 - 用户触发某个事件 - 调用某段JS - 加密函数 - 给服务器发信息（XHR-SEND） - 接收到服务器数据 - 解密函数 - 刷新网页渲染
```

示例：https://oauth.d.cn/auth/goLogin.html

##### 3.1.1 DOM事件断点

+ 执行的比较靠前 距离加密函数比较远

##### 3.1.2 XHR断点

+ 执行比较靠后 距离加密函数相对较近   可以根据栈快速定位

  **注意**：非XHR发送的就断不住
  
  

### 4 方法栈

 **栈是一种先进后出的特殊线性表结构**

调用栈是解析器的一种机制，可以在脚本调用多个函数时，通过这种机制，我们能够追踪到哪个函数正在执行，执行的函数体又调用了哪个函数。

- 当脚本要调用一个函数时，解析器把该函数添加到栈中并且执行这个函数。
- 任何被这个函数调用的函数会进一步添加到调用栈中，并且运行到它们被上个程序调用的位置。
- 当函数运行结束后，解释器将它从堆栈中取出，并在主代码列表中继续执行代码。

**4.1 代码说明**

```javascript
function ps(a,b){
    return a+b
}

function pn(a,b){
    var xx = ps(a,b)
    return xx / 2
}
num = pn(1,2)
console.log(num)
```



### 5 debug原理

案例地址：https://gaokao.chsi.com.cn/zyk/zybk/

+ 无限debbugger不会真正得死循环，而是有规律得执行逻辑，一般用定时器

```javascript
Function("debugger;").call()
```



#### 5.1.0 样例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>

<h1 id="box"></h1>

<body>

<script>
    var ss = document.getElementById('box')
    function ff() {
        debugger;
    }
    setInterval(ff,100);

    ss.innerHTML = "大家晚上好";

</script>
</body>
</html>

```

#### 5.1.1 浏览器过debugger

​	1，当定义器运行到这个`debugger`这个代码的时候，那么这个时候它为`true`，它肯定执行我们的`debugger`代码，那我们可以用浏览器的功能给他改成`false`

 ![image-20220810162631398](images\image-20220810162631398.png)

2，编辑断点

```
写个1===0的先验条件，永远为假，就永远不会进入这个断点了。
```

#### 5.1.2 方法置空

无限debugger产生的原因是第七行代码`ff`这个函数造成的,所以我们可以重写这个函数,使无限debugger失效.在控制台中输入`function ff(){}`即可,如图:

注：一定要在debugger进入之前

 ```js
setInterval_ba = setInterval
setInterval = function ff(){}
 ```



#### 5.1.3 修改响应文件

把JS文件保存到本地修改，修改范围主要是将debugger相关的代码删除或者改写，可以使用文件替换、抓包工具拦截方式



####  5.1.4 注入代码到JS文件

在控制台注入代码

站点：https://bz.zzzmh.cn/index

```js
var _constructor = constructor;
Function.prototype.constructor = function(s) {
    
    if (s == "debugger") {
        console.log(s);
        return null;
    }
    return _constructor(s);
}
```



### 6  hook技术

Hook 是一种钩子技术，在系统没有调用函数之前，钩子程序就先得到控制权，这时钩子函数既可以加工处理（改变）该函数的执行行为，也可以强制结束消息的传递。简单来说，修改原有的 JS 代码就是 Hook。

**Hook 技术之所以能够实现有两个条件：**

- 客户端拥有 JS 的最高解释权，可以决定在任何时候注入 JS，而服务器无法阻止或干预。服务端只能通过检测和混淆的手段，另 Hook 难度加大，但是无法直接阻止。
- 除了上面的必要条件之外，还有一个条件。就是 JS 是一种弱类型语言，同一个变量可以多次定义、根据需要进行不同的赋值，而这种情况如果在其他强类型语言中则可能会报错，导致代码无法执行。js 的这种特性，为我们 Hook 代码提供了便利。



**注意：**JS 变量是有作用域的，只有当被 hook 函数和 debugger 断点在同一个作用域的时候，才能 hook 成功。



#### 6.1 *Hook步骤：*

+ 1 寻找hook的点

+ 2 编写hook逻辑

+ 3 调试

**注**：最常用的是`hook cookie`



#### 6.2 hook 方法

站点：https://www.wcbchina.com/login/login.html

我们知道在 `JavaScript` 中 `JSON.stringify()` 方法用于将 JavaScript 对象或值转换为 JSON 字符串，`JSON.parse()` 方法用于将一个 JSON 字符串转换为 JavaScript 对象，某些站点在向 web 服务器传输用户名密码时，会用到这两个方法

```javascript
(function() {
    var stringify = JSON.stringify;
    JSON.stringify = function(ps) {
        
        console.log("Hook JSON.stringify ——> ", ps);
        debugger;
        return stringify(ps);
    }
})();
```

首先定义了一个变量 `stringify` 保留原始 `JSON.stringify` 方法，然后重写 `JSON.stringify` 方法，遇到 `JSON.stringify` 方法就会执行 `debugger` 语句，会立即断下，最后将接收到的参数返回给原始的 `JSON.stringify` 方法进行处理，确保数据正常传输



#### 6.3 hook  XHR请求

**案例地址：**https://www.qimai.cn

定义了一个变量 `open` 保留原始 `XMLHttpRequest.open` 方法，然后重写 `XMLHttpRequest.open` 方法，判断如果 rnd 字符串值在 URL 里首次出现的位置不为 -1，即 URL 里包含 `analysis`字符串，则执行 `debugger` 语句，会立即断下。

```javascript
// 如果是正数 表示存在里面
// 如果是-1 表示不在里面

(function () {
    var open = window.XMLHttpRequest.prototype.open;
    window.XMLHttpRequest.prototype.open = function (method, url, async) {
        if (url.indexOf("analysis") != -1) {
            debugger;
        }
        return open.apply(this, arguments);
    };
})();
```

**Interceptors**-拦截器

+ 请求拦截器：在发送请求之前，可以借助一些函数来对请求的内容和参数做一些检测。若有问题可以直接取消请求。
+ 响应拦截器：当服务器返回响应数据时，响应拦截器会在我们拿到结果前预先处理响应数据。例如对响应数据做一些格式化处理，或者当响应失败时，可以做一些失败提醒和纪录。

```javascript
// npm install axios
axios = require('axios')
//设置请求拦截器
axios.interceptors.request.use(function (config) {
    console.log('请求拦截器 成功')
    config.timeout = 2000; //修改请求config
    config.headers['sign'] = 'lili'
    return config;
}, function (error) {
    console.log('请求拦截器 失败')
    return Promise.reject(error);
});

//设置响应拦截器
axios.interceptors.response.use(function (response) {
    console.log('响应拦截器 成功')
    console.log('调解密函数进行解密数据')
    //return response;
    return response.data; //修改响应数据
}, function (error) {
    console.log('响应拦截器 失败')
    return Promise.reject(error);
});

//发送请求
axios.get('http://httpbin.org/get').then(res=>console.log(res))
```



#### 6.4 HOOK cookie操作

WEBAPI地址：https://developer.mozilla.org/zh-CN/docs/Web/API

`Object.defineProperty `为对象的属性赋值，替换对象属性

基本语法：`Object.defineProperty(obj, prop, descriptor)`，它的作用就是直接在一个对象上定义一个新属性，或者修改一个对象的现有属性，接收的三个参数含义如下：

+ `obj`：需要定义属性的当前对象；

+ `prop`：当前需要定义的属性名；

```javascript
Object.defineProperty(user,"age",{
 get:function(){
      console.log("这个人来获取值了！！");
      return count;
 },
    
 set:function(newVal){
      console.log("这个人来设置值了！！");
      count=newVal+1;
 }
})
```

**cookie 示范**

示范例子：http://q.10jqka.com.cn/

cookie 钩子用于定位 cookie 中关键参数生成位置，以下代码演示了当 cookie 中匹配到了 `v`， 则插入断点：

```JavaScript
(function () {
  var cookieTemp = '';
  Object.defineProperty(document, 'cookie', {
    set: function (val) {
      if (val.indexOf('v') != -1) {
        debugger;
      }
      console.log('Hook捕获到cookie设置->', val);
      cookieTemp = val;
      return val;
    },
    get: function () {
      return cookieTemp;
    },
  });
})();
```

注：正常`hook cookie`操作的时候需要清除下`cookie`



### 7 python执行JS的方式

##### 7.1 PyExecJS

地址;https://github.com/doloopwhile/PyExecJS

PyExecJS 是使用最多的一种方式，底层实现方式是：在本地 JS 环境下运行 JS 代码

```python
pip install PyExecJS 
```

7.1.1 读取JS代码

```python
with open(file_name, 'r', encoding='UTF-8') as file:
	result = file.read()
```

7.1.2 execjs 类的compile()方法编译加载上面的 JS 字符串，返回一个上下文对象

```python
context1 = execjs.compile("这里面是JS代码")
```

7.1.3 调用上下文对象的call() 方法执行 JS 方法

```python
result1 = context1.call("函数", "参数1", "参数2")
```

需要注意的，由于 PyExecJS 运行在本地 JS 环境下，使用之前会启动 JS 环境，最终导致运行速度会偏慢

7.1.4 eval执行

eval() 函数计算 JavaScript 字符串，并把它作为脚本代码来执行。

```javascript
print(execjs.eval('Date.now()'))
```



### 8 浏览器环境补充方法

https://www.runoob.com/jsref/obj-window.html

```javascript
document = {
    cookie:'uuid_tt_dd=10_29360271920-1658044222535-945484; __gads=ID=5b925b796ab29466-22740a5938d50041:T=1658044224:RT=1658044224:S=ALNI_MYZZ3qnATdjgh4YHRlZaBk3TnwTFw; p_uid=U010000',
    location : {
        href:'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=87135040_oem_dg&wd=eval%20JS%20&fenlei=256&oq=eval&rsv_pq=e1b3f2520003297e&rsv_t=7e58%2ByqRgVEysyNAVRctyGmKUct9An%2B6da7wzdVJDXgo7qaAS1DKyn86mLazGA1IqBPpY359&rqlang=cn&rsv_dl=tb&rsv_enter=1&rsv_btype=t&inputT=860&rsv_sug3=56&rsv_sug1=35&rsv_sug7=100&rsv_sug2=0&rsv_sug4=1037'
    }
}

navigator = {userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

window = {
    document : document,
    navigator:navigator
}
console.log(document.location.href);
document.getElementsByTagName = function(){};
```

