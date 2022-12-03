


# pip install websockets

import websockets
import asyncio

# 发送  加密参数
async def echo(websocket):
    message = '我是发送给客户端的信息'
    # 发送数据
    await  websocket.send(message)
    return  True

# 接收  客户端返回的数据
async def recv_msg(websocket):
    while 1:
        # 接收
        resv_text = await websocket.recv()
        print(resv_text)


async def main_run(websocket):
    await echo(websocket)
    await recv_msg(websocket)


stat_sever = websockets.serve(main_run,'127.0.0.1',9999)
print('成功建立连接')
loop = asyncio.get_event_loop()
loop.run_until_complete(stat_sever)

# 保持长连接 需要不断的监听返回的数据
loop.run_forever()



