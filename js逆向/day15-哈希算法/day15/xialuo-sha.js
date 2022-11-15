
// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function SHA1Encrypt() {
    var text = "12312312"
    return CryptoJS.SHA384(text).toString();
}

console.log(SHA1Encrypt())
// faec670ce75fe79cae1fa899617818031b1f201c  40

