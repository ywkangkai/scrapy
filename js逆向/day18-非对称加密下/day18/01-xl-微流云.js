
// npm install jsencrypt --save   可以实现  JSEncrypt()
JSEncrypt = require('jsencrypt')
var CryptoJS = require('crypto-js')

function get_pwd(pwds,item1,itme2){
    var encrypt = new JSEncrypt();
    encrypt.setPublicKey(item1);
    var encrypted = encrypt.encrypt(itme2 + CryptoJS.SHA512(pwds).toString());
    return encrypted
}









