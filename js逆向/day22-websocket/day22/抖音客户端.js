

// i.toObject()    浏览器不需要定义window

window.dataxl = i.toObject()
!function (){
    var res = window.dataxl
    var ws = new WebSocket('ws://127.0.0.1:9999')
    window.wsXl = ws;
    ws.open = function (evt){}
    ws.onmessage = function (evt){
        ws.send(JSON.stringify(res))
    }
}();


// sha256('12321321')
// window.dataxl = sha256
// ws.send(JSON.stringify(window.dataxl))


!function (){
        if (window.xx) {}
        else {
            //  导出算法
            window.dataxl = f;
            // 连接服务器
            var ws = new WebSocket('ws://127.0.0.1:9999')
            // 导出连接对象
            window.wsxl = ws;
            // 建立一个标记
            window.xx = true
            // 接收服务器传的数据  获取后台使用 evt.data
            ws.onmessage = function (evt){
                // evt 接收服务器传密文数据
                var xl = evt.data
                // 使用JS方法进行解密操作
                var res = window.dataxl(xl)
                // 前端给后端发送数据
                ws.send(JSON.stringify(res))
            }
        }
}();
