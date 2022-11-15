

// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function MD5Test() {
    var text = '12312312'
    return CryptoJS.MD5(text).toString()
}

console.log(MD5Test());

// 220466675e31b9d20c051d5e57974150  32
