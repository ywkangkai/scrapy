var CryptoJS = require('crypto-js')

navigator = {
    appVersion:'5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

r = function(e) {
        var t = CryptoJS.MD5(navigator.appVersion).toString()
          , r = "" + (new Date).getTime()
          , i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: CryptoJS.MD5("fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5").toString()
        }
    };

console.log(r('hello'));


