
var ps;

!function (t) {
    // 加载器
    var e = {};
     function i(n) {
        if (e[n])
            return e[n].exports;
        var s = e[n] = {
            i: n,
            l: !1,
            exports: {}
        };
        return t[n].call(s.exports, s, s.exports, i),
        s.l = !0,
        s.exports
    }
    // i(200)
    ps = i

}({
    'xl':function (){
        console.log('asdasdas')
        return "asd"
    },

    100: function(t, e, i) {
        console.log('对密码进行加密')
        return 'hello world'
    },
    200: function (){
        console.log('对密码进行解密')
    }

})

console.log(ps(100));








