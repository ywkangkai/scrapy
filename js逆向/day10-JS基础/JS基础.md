## JavaScript逆向基础

#### 学习收获

+ 爬虫对抗的参数加密
+ JavaScript基本语法
+ JavaScript作用域
+ JavaScript函数编写



### 1 逆向声明

#### 1.1 为什么要学逆向

+ 头部签名验证
  + aHR0cHM6Ly93d3cub2tsaW5rLmNvbS96aC1jbi9idGMvdHgtbGlzdD9saW1pdD0yMCZwYWdlTnVtPTE=
+ 请求参数签名验证
  + aHR0cHM6Ly93d3cucWltYWkuY24vcmFuay9pbmRleC9icmFuZC9mcmVlL2RldmljZS9pcGFkL2NvdW50cnkvY24vZ2VucmUvMzY=
+ cookie验证
  + aHR0cHM6Ly93d3cuZHNlZHQuZ292Lm1vL3poX0NOL3BnX2hvbWU=
+ 响应数据验证
  + aHR0cHM6Ly9nZ3p5ZncuZmouZ292LmNuL2J1c2luZXNzL2xpc3Qv



### 2.  JavaScript 是脚本语言

+ JavaScript 是一种轻量级的编程语言。

+ JavaScript 是可插入 HTML 页面的编程代码。

+ JavaScript 插入 HTML 页面后，可由所有的现代浏览器执行。

+ JavaScript 很容易学习



### 3. 如何在Pycharm里面运行JS

任何的编程语言想要执行都需要有一个好的环境，python如此、JavaScript也是如此。

#### 3.1 node

```
Node.js 是一个基于 Chrome V8 引擎的 JavaScript 运行
```

**下载：**http://nodejs.cn/download/



### 4. JavaScript语法

#### 4.1 注释

```
单行注释以 // 开头
多行注释以 /* 开始，以 */ 结尾
```



#### 4.2 变量和数据类型

与代数一样，JavaScript 变量可用于存放值（比如 x=5）和表达式（比如 z=x+y）。

JavaScript 变量有很多种类型，但是现在，我们只关注数字和字符串

```javascript
var pi=3.14;  
// 如果你熟悉 ES6，pi 可以使用 const 关键字，表示一个常量
// const pi = 3.14;
var person="John Doe";
var answer='Yes I am!';
```

##### 4.2.1 声明（创建） JavaScript 变量

我们使用 var 关键词来声明变量：

```javascript
// 先声明 再赋值
var carname;
carname="Volvo";
// 声明变量时对其赋值
var carname="Volvo";
```

##### 4.2.2 一条语句，多个变量

可以在一条语句中声明很多变量。该语句以 var 开头，并使用逗号分隔变量即可：

```
var lastname="Doe", age=30, job="carpenter";
```

##### 4.3.3  let 和 const

`ES2015(ES6)` 新增加了两个重要的 `JavaScript `关键字: **let** 和 **const**。

+ `let` 声明的变量只在` let` 命令所在的代码块内有效。

+ `const` 声明一个只读的常量，一旦声明，常量的值就不能改变。

**注意：**var是函数[作用域](https://so.csdn.net/so/search?q=作用域&spm=1001.2101.3001.7020)，let是块作用域。块作用域由 { } 包括；



1、let不能被重新定义，但是var是可以的

```JavaScript

let dogs = "狗"
let dogs = "猫"
console.log(dogs)

var dog = "狗"
var dog = "猫"
console.log(dog)
```

2、***声明的变量具有块作用域（局部变量）的特征***

```javascript
{ var age = 18
  console.log(age)
}
console.log(age)

{ let cat = "猫"
  console.log(cat)
}
console.log(cat)
```

`var`声明的变量存在变量提升（将变量提升到当前作用域的顶部）。即变量可以在声明之前调用，值为`undefined`。
`let`和`const`不存在变量提升。即它们所声明的变量一定要在声明后使用，否则报`ReferenceError`错

**总结：**

1. **var** 声明的变量属于函数作用域
2. **var** 声明的变量存在提升（hoisting）
3. **var** 变量可以重复声明



#### 5. 对象

对象也是一个变量，但对象可以包含多个值（多个变量），每个值以 **name:value** 对呈现。

```javascript
var car = {name:"xialuo", model:500, color:"white"};
```

创建了对象的一个新实例

```javascript
person= new Object();
person.firstname="John";
person.lastname="Doe";
person.age=50;
```



##### 5.1 对象访问

```javascript
car.name;
car['name']
```

##### 5.2 对象方法

对象的方法定义了一个函数，并作为对象的属性存储。

 ```javascript
var person = {
    firstName: "xl",
    lastName : "lili",
    id : 5566,
    fullName : function()
	{
       return this.firstName + " " + this.lastName;
    }
};
 ```

**注:**在对象方法中， `this` 指向调用它所在方法的对象。



#### 6. JavaScript 函数语法

函数就是包裹在花括号中的代码块，前面使用了关键词 function：

```javascript
function functionname()
{
    // 执行代码
}
```

**注：** JavaScript 对大小写敏感。关键词 function 必须是小写的，并且必须以与函数名称相同的大小写来调用函数。

##### 6.1 有名函数

```javascript
function xxs(){
    console.log('123')
}
xxs();
```

##### 6.2 函数赋值表达式定义函数

```javascript
sss = function (a,b,c){
    console.log(b)
}
sss(1)
```

##### 6.3 JavaScript之自执行函数

一种理解是，自执行即自动执行，也就是所谓的立即执行函数

```javascript
!(function () {
  console.log("Hello World!");
})();
```

在前面加上一个布尔运算符（只多了一个感叹号），就是表达式了，将执行后面的代码

##### 6.4 内部函数外部调用

```javascript
var _xl;
!(function () {
    function xl(){
        console.log('hello')
    }
    _xl = xl;
})();
_xl()
```



#### 7. 作用域

变量在函数内声明，变量为局部变量，具有局部作用域。

局部变量：只能在函数内部访问

变量在函数外定义，即为全局变量。

```javascript
as = 123
function xxss(){
    console.log(as)
    var ddd = 10;
}
console.log(as)
```



##### 7.1 JavaScript 变量生命周期

+ JavaScript 变量生命周期在它声明时初始化。

+ 局部变量在函数执行完毕后销毁。

+ 全局变量在页面关闭后销毁。



#### 8 JavaScript事件

HTML 事件是发生在 HTML 元素上的事情。

当在 HTML 页面中使用 JavaScript 时， JavaScript 可以触发这些事件。

##### 8.1 登陆举例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<input type="text" id="name">
<input type="text" id="pwd">
<button onclick="xl()">登陆</button>

<script>
    function xl(){
         var name = document.getElementById("name").value
         var pwd = document.getElementById("pwd").value
        console.log(name,pwd)
    }
</script>

</body>
</html>
```

#### 9 json转换

```javascript
JSON.parse()	    // 用于将一个 JSON 字符串转换为 JavaScript 对象。
JSON.stringify()	// 用于将 JavaScript 值转换为 JSON 字符串。
```

注：经常使用在数据的处理方面，比如后台返回数据。所以后台返回的加密数据，可以使用分析`JSON.parse` 来找加密位置   体现在请求后

注：`JSON.stringify` 用在数据加密后，变成字符串传给后台服务器    		体现在请求前

##### 实例演示

```javascript
// 要实现从JSON字符串转换为JS对象，使用 JSON.parse() 方法
var obj = JSON.parse('{"a": "Hello", "b": "World"}')
// 要实现从JS对象转换为JSON字符串，使用 JSON.stringify() 方法：
var json = JSON.stringify({a: 'Hello', b: 'World'});
```



10 无限debugger

```javascript
var _constructor = constructor;
Function.prototype.constructor = function(s) {
    if (s == "debugger") {
        console.log(s);
        return null;
    }
    return _constructor(s);
}
```

