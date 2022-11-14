

// 学习语法结构

window = {}
location = {
    href:'https://www.expressjs.com.cn/starter/hello-world.html'
}


navigator = {
    userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

window = {
    location:location,
    navigator:navigator,
    document :{
        cookie:'Hm_lvt_194f83d7eb0049a9ca1ae2d4b2d04c33=1667896212,1668169177; Hm_lpvt_194f83d7eb0049a9ca1ae2d4b2d04c33=1668169340',
    }
}


function ps(){
    if(window['location'].href=='https://www.expressjs.com.cn/starter/hello-world.html'){
        // 真实结果
        return 'hello world'
    }else {
        // 假数据
        return 'hello'
    }
}

console.log(window.navigator.userAgent);
console.log(window.document.cookie);

console.log(ps());






