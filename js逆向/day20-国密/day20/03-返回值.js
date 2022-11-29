

function get_header(){

    // 返回头部信息
    var headers = {}
    return headers['x1'] = '张三',
        headers['x2'] = '李四',
        headers['x3'] = '王五',
        headers
}

console.log(get_header());
