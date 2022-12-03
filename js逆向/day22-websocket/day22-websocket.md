# websocket通讯

**说明**

```
本教程仅供学习交流使用，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关，请各学员自觉遵守相关法律法规。
```



## 1 简介

### 一，什么是websocket

- WebSocket是HTML5下一种新的协议（websocket协议本质上是一个基于tcp的协议）
- 它实现了浏览器与服务器全双工通信，能更好的节省服务器资源和带宽并达到实时通讯的目的
- Websocket是一个**持久化**的协议



### 二，websocket的原理

+ websocket约定了一个通信的规范，通过一个握手的机制，客户端和服务器之间能建立一个类似tcp的连接，从而方便它们之间的通信
+ 在websocket出现之前，web交互一般是基于http协议的短连接或者长连接
+ websocket是一种全新的协议，不属于http无状态协议，协议名为"ws"



### 三，websocket与http的关系

![image-20221127202959653](images\image-20221127202959653.png)

 **相同点：**

1. **都是基于tcp的，都是可靠性传输协议**
2. **都是应用层协议**



**不同点：**

1. **WebSocket是双向通信协议，模拟Socket协议，可以双向发送或接受信息**
2. **HTTP是单向的**
3. **WebSocket是需要浏览器和服务器握手进行建立连接的**
4. **而http是浏览器发起向服务器的连接，服务器预先并不知道这个连接**



**联系：**

- **WebSocket在建立握手时，数据是通过HTTP传输的。但是建立之后，在真正传输时候是不需要HTTP协议的**



**总结（总体过程）：**

+ **首先，客户端发起http请求，经过3次握手后，建立起TCP连接；http请求里存放WebSocket支持的版本号等信息，如：Upgrade、Connection、WebSocket-Version等；**
+ *然后，服务器收到客户端的握手请求后，同样采用HTTP协议回馈数据；*
+ **最后，客户端收到连接成功的消息后，开始借助于TCP传输信道进行全双工通信。**



### 四，websocket解决的问题

#### 4.1.http存在的问题
http是一种无状态协议，每当一次会话完成后，服务端都不知道下一次的客户端是谁，需要每次知道对方是谁，才进行相应的响应，因此本身对于实时通讯就是一种极大的障碍
http协议采用一次请求，一次响应，每次请求和响应就携带有大量的header头，对于实时通讯来说，解析请求头也是需要一定的时间，因此，效率也更低下
最重要的是，需要客户端主动发，服务端被动发，也就是一次请求，一次响应，不能实现主动发送



#### 4.2 websocket的改进
一旦WebSocket连接建立后，后续数据都以帧序列的形式传输。在客户端断开WebSocket连接或Server端中断连接前，不需要客户端和服务端重新发起连接请求。在海量并发及客户端与服务器交互负载流量大的情况下，极大的节省了网络带宽资源的消耗，有明显的性能优势，且客户端发送和接受消息是在同一个持久连接上发起，实现了“真·长链接”，实时性优势明显。

![image-20221127214541767](images\image-20221127214541767.png)

**WebSocket有以下特点：**

是真正的全双工方式，建立连接后客户端与服务器端是完全平等的，可以互相主动请求。而HTTP长连接基于HTTP，是传统的客户端对服务器发起请求的模式。
HTTP长连接中，每次数据交换除了真正的数据部分外，服务器和客户端还要大量交换HTTP header，信息交换效率很低。Websocket协议通过第一个request建立了TCP连接之后，之后交换的数据都不需要发送 HTTP header就能交换数据，这显然和原有的HTTP协议有区别所以它需要对服务器和客户端都进行升级才能实现（主流浏览器都已支持HTML5）



### 示例：

1、抖音直播、虎牙直播

![image-20221127215151915](images\image-20221127215151915.png)





## 2 实操使用

### 2.1 客户端

#### 3.3 处理方法

```javascript
//连接发生错误的回调方法
websocket.onerror = function () {
    setMessageInnerHTML("WebSocket连接发生错误");
};

//连接成功建立的回调方法
websocket.onopen = function () {
    setMessageInnerHTML("WebSocket连接成功");
}

//接收到消息的回调方法  接服务器信息的方法
websocket.onmessage = function (event) {
    setMessageInnerHTML(event.data);
}

//连接关闭的回调方法
websocket.onclose = function () {
    setMessageInnerHTML("WebSocket连接关闭");
}
```

### 2.2 服务端

```python
pip install websockets
```

+ connect: 在client端使用，用于建立连接。

+ send:发送数据，server和client双方都可以使用。

+ [recv](https://so.csdn.net/so/search?q=recv&spm=1001.2101.3001.7020):接收数据，server和client双方都可以使用。

+ close:关闭连接，server和client双方都可以使用。

```python
    # encoding: utf-8
    import asyncio
    import websockets
    
    async def echo(websocket):
        # 使用WebSocket在客户端和服务器之间建立全双工双向连接后，就可以在连接打开时调用send()方法。
        message = 'hello world'
        # 发送数据
        await websocket.send(message)
        return True
    
    async def recv_msg(websocket):
        while 1:
            # 接收数据
            recv_text = await websocket.recv()
            print(recv_text)
    
    async def main_logic(websocket,path):
        await echo(websocket)
        await recv_msg(websocket)
    
    start_server = websockets.serve(main_logic, '127.0.0.1', 8080)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server)
    # 创建了一个连接对象之后，需要不断监听返回的数据，则调用 run_forever 方法，要保持长连接即可
    loop.run_forever()

```



## 3 案例实操

分析参数时，可以根据关键词搜索，因为JS里面websocket是固定的，比如搜索`message、on_message、onmessage、on_open、onopen、ws.send、`等，可以快速定位。

JS 里面`new WebSocket()` 是固定的语法



1、搜索全局关键字、可以看到有监听消息位置

![image-20221128145527260](images\image-20221128145527260.png)

2、进去后看监听方法，接收到服务器的数据响应`r.toobject()`，里面的数据是加密的

![image-20221128145727636](images\image-20221128145727636.png)



`emit方法`用于实现服务器向客户端广播事件，可以从这个位置跟进去查看数据

![image-20221128150017502](images\image-20221128150017502.png)



从这里执行数据解密服务，`i.toObject`可以获取数据

![image-20221128145326513](images\image-20221128145326513.png)



## 4 处理加密数据

使用socket处理网站算法、可以导出加密逻辑进行转发，做到无视加密算法。

![image-20221128162538848](images\image-20221128162538848.png)

可以在里面下连接





































