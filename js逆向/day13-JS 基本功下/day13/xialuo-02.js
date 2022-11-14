
document = {}
// 'asdasdasdqwer' 来自于JS生成
document.cookie = 'asdasdasdqwer'

// JS加密某个参数 需要给document.cookie 进行赋值  所以可以断点到 document.cookie

// 对象
var user = {}
user.name = '丽丽'
console.log(user);
// Object.defineProperty(user,'name',{
//     value:'xxx'
// })
// console.log(user);


// get  获取
// set  设置或者修改
var age = 18
Object.defineProperty(user,'count',{
   get:function (){
       return age
   },
    set:function (val){
             age = val + 1
    }
})
console.log(user.count);  // 18
user.count = 30
console.log(user.count);











