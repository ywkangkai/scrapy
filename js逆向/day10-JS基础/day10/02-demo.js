
// 函数  代码块

/*
function ps(//传递参数) {
// 写业务逻辑
}
*/


function ps (a,b,c,d,e){
    console.log(a + b)
}

// 调函数
ps('1','2')


// // 调函数
// pn('3','4')

var pn = function (a,b) {
     console.log(a + b)
}

// 调函数
// pn('3','4')


!(function (a,b){
    console.log('hello world')
    console.log(a+b)
})('1','2')
// 自执行函数  自动触发  不需要你去调用



var xlssss;
!(function (){
    console.log('我触发了')
    function xl(){
        console.log('我是内部函数')
    }
    xlssss = xl
})()
// xlssss();


var xxa = 20   // 函数外声明的是 全局变量
function demo(){
    // 函数内部声明的是局部
    console.log('hello')
    console.log(xxa);
    var c = 10;
}
// console.log(ddd);
console.log(xxa);
// demo()
// console.log(c);  // 不行的

// : c is not defined   经常的出现的错误































