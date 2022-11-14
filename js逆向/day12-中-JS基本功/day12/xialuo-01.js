
function ps(a,b){
    return a+b
}

function pn(a,b){
    var xx = ps(a,b)
    return xx / 2
}
num = pn(1,2)
console.log(num)




(function() {
    var stringify = JSON.stringify;
    JSON.stringify = function(params) {
        // 这个是针对 JSON.stringify用得多得场景，可以细化到参数
        if (params.password) {
            debugger
        }
        console.log("Hook JSON.stringify ——> ", params);
        // debugger;
        return stringify(params);
    }
})();





