
var CryptoJS = require('crypto-js')

rndString = function() {
        for (var e = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz", t = "", n = 0; n < 16; n++) {
            var a = Math.floor(Math.random() * e.length);
            t += e.substring(a, a + 1)
        }
        return t
    }


    function desEncrypt(e, t) {
    var _iv = 'k1fsa01v';
        var n = CryptoJS.enc.Utf8.parse(t);
        return CryptoJS.DES.encrypt(e, n, {
            // iv: CryptoJS.enc.Utf8.parse(_iv),
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        }).toString()
    }


console.log(desEncrypt('{"username":"asdasdasd","password":"234234234","captcha":"13370"}', rndString()));
