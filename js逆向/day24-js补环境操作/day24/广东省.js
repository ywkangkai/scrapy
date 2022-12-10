const by = "zxcvbnmlkjhgfdsaqwertyuiop0987654321QWERTYUIOPLKJHGFDSAZXCVBNM"
var aK = by + "-@#$%^&*+!";

function sK(e, t) {
    switch (arguments.length) {
    case 1:
        return parseInt(Math.random() * e + 1, 10);
    case 2:
        return parseInt(Math.random() * (t - e + 1) + e, 10);
    default:
        return 0
    }
}
function lK(e) {
    return [...Array(e)].map(()=>by[sK(0, 61)]).join("")
}

n = lK(16)


console.log(n)

function sr(e=[]) {
    return e.map(t=>aK[t]).join("")
}

o = sr([8, 28, 20, 42, 21, 53, 65, 6])

// 标准的sha256算法


