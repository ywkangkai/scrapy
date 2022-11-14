const express = require('express')
const app = express()
const port = 5001  // 程序运行的端口


function ps(){
    return '我是逆向的加密结果！'
}

function pn(val){
    // 环境差异
    pwd = btoa(val)
    return pwd
}


app.get('/', (req, res) => {
    var data = ps()
  res.send(data)
})


app.get('/api', (req, res) => {
    var params = req.query
        console.log(params);
    // 这里是取值
    info = pn(params.pwd)

    res.send(info)
})


app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})










