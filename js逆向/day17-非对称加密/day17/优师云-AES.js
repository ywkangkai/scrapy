
var CryptoJS = require('crypto-js')
i = {}
i.a = CryptoJS

function get_pwd(val){
        r = CryptoJS.enc.Latin1.parse('password.yunjy.y');
        var n = r
          , a = CryptoJS.AES.encrypt(val, r, {
            iv: n,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.ZeroPadding
        });
        return a.toString()
}

console.log(get_pwd('123123'));


//  盲猜  关键字 算法  hook  xhr断   ast内存漫游



