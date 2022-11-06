
var a = '夏洛'
console.log(a)

 //  == print(a)  单行注释

/*
我是多行注释
我是多行注释
  */


var pi=3.14;
var person="John Doe";
answer='Yes I am!';

// 声明多个变量
var lastname="Doe", age=30, job="carpenter";

// var  ES5的
// let const ES6新增

var  xxx = 100
xxx = 200
console.log(xxx);


let dog = "狗"
// let dogs = "猫"   // 不能重新定义
console.log(dog)

var dogs = "狗"
var dogs = "猫"   // 不能重新定义
console.log(dogs)


// 块作用域
{
    var age = 18
    console.log(age)
}
console.log(age);


{
    let ages = 18
    console.log(ages)
}
// console.log(ages);

console.log(qwe)
var qwe = 10
console.log(qwe)

// 扣JS代码 有必要在乎先后顺序吗？  没必要  变量放最上边


// 对象   {}
var car = {name:"xialuo", model:500, color:"white"};
console.log(car.name);



person= new Object()
person.firstname="John"
person.lastname="Doe"
person.age=50
console.log(person)
console.log(typeof person)


var Persor = {
    name:"xialuo",
    age : '18',
    ps : function () {
        return this.name + this.age
    }
}
pn = Persor.ps()
console.log(pn);
//  self  this  谁调用指向谁



// 对象取值
Persor.name
Persor['age']


















