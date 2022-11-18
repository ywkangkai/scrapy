var CryptoJS = require('crypto-js')

function HMACEncrypt() {
    var text = "I love python!"
    var key = "secret111"   // 密钥文件
    // return CryptoJS.HmacMD5(text, key).toString();
    // return CryptoJS.HmacSHA1(text, key).toString();
    return CryptoJS.HmacSHA256(text, key).toString();
}
console.log(HMACEncrypt())


