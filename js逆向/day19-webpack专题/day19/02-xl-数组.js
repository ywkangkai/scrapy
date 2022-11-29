var pn;

!function (t){
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
    // i(0)
    pn = i

}([
    function (e,t,i){
        console.log('123123')
    },
      function (e,t,i){
        console.log('我是解密函数')
    },

])

pn(1)

