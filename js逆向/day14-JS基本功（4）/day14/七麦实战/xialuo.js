

/*
    analysis = (0,i[jt])((0,i[qt])(a, d))
    (0,i[jt])((0,i[qt])(a, d)) = i[jt](i[qt](a, d))

    arg1 =  i[qt](a, d)
    analysis = i[jt](arg1)

    a = 'MTEyMDIyLTExLTExMzZjbmZyZWVpcGFk@#/rank/indexSnapshot@#6948635722@#3'
    d = 'xyz517cda96abcd'

    还原入口参数   a  d
      a =






JS 里面称为补参数
他是把参数 做了名字混淆


扣JS
    遇到需要还原的 就还原
    遇到调函数 就补函数
    总结一句话 缺啥补啥

* */

ppp = {}

 function o(n) {
        t = '',
        ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65']['forEach'](function(n) {
            t += unescape('%u00' + n)
        });
        var t, e = t;
        return String["fromCharCode"](n)
    }
function h(n, t) {
    t = t || u();
    for (var e = (n = n['split'](''))['length'], r = t['length'], a = 'charCodeAt', i = 0; i < e; i++)
        n[i] = o(n[i][a](0) ^ t[(i + 10) % r][a](0));
    return n['join']('')
}

a = 'MTEyMDIyLTExLTExMzZjbmZyZWVpcGFk@#/rank/indexSnapshot@#6948635722@#3'
d = 'xyz517cda96abcd'
    // console.log(h(a, d));
// arg1 = h(a, d)
// analysis = i[jt](arg1)

function v(t) {
                t = encodeURIComponent(t)['replace'](/%([0-9A-F]{2})/g, function(n, t) {
                    return o('0x' + t)
                });
                try {
                    return btoa(t)
                } catch (n) {
                    return Buffer.from(t)['toString']('base64')
                }
            }

// console.log(v(arg1));
ppp.xx = v
// 还原入口 封装

function y(n, t, e) {
    for (var r = void 0 === e ? 2166136261 : e, a = 0, i = n['length']; a < i; a++)
        r = (r ^= n['charCodeAt'](a)) + ((r << 1) + (r << 4) + (r << 7) + (r << 8) + (r << 24));
    return t ? ('xyz' + (r >>> 0)['toString'](16) + 'abcd')['substr'](-16) : r >>> 0
}

function ps(){
    var v = '@#'
    var url = "/rank/index"
    var baseurl = 'https://api.qimai.cn'
    var s = 2104
    var r = +new Date - (s || 0) - 1661224081041
    a = ['free', 'ipad', 'cn', '36']
    a = a['sort']()['join']('')
    a = ppp.xx(a)
    a = (a += v + url['replace'](baseurl, '')) + (v + r) + (v + 3)
    console.log(a);
    d = y('qimai@2022&Technology', 1)

    arg1 = h(a, d)
    analysis = ppp.xx(arg1)
    console.log(analysis);

}

ps()




