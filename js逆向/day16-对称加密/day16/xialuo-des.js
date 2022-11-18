var CryptoJS = require('crypto-js')

function desEncrypt() {
    var key = CryptoJS.enc.Utf8.parse(desKey),
        iv = CryptoJS.enc.Utf8.parse(desIv),
        srcs = CryptoJS.enc.Utf8.parse(text),
        // CBC 加密模式，Pkcs7 填充方式
        encrypted = CryptoJS.DES.encrypt(srcs, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
    return encrypted.toString();
}

var text = "I love Python!"       // 待加密对象
var desKey = "6f726c64f2c2057"    // 密钥
var desIv = "0123456789ABCDEF"    // 初始向量
var encryptedData = desEncrypt()
console.log(encryptedData);
