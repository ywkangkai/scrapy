
# pip install websockets

import websockets
import asyncio
import requests
# 发送  加密参数

def req_html():
    # 写翻页功能
    res = requests.get('https://api.waitwaitpay.com/api/vendors/nearby?keyword=%E7%82%B8%E9%B8%A1&latitude&longitude&page=1&request_id=-1&type=search&with_vouchers=false',headers={
        'user-agent':'adasdasdasd'
    })
    return res

async def echo(websocket):
    message = '我是发送给客户端的信息'
    # 发送数据
    # 可以给他传 密文  发送给浏览器解密
    res = req_html()
    sent_text = res.text
    await  websocket.send(sent_text)
    return  True

# 接收  客户端返回的数据
async def recv_msg(websocket):
    while 1:
        # 接收
        resv_text = await websocket.recv()
        print(resv_text)
        with open('sss.txt','w',encoding='utf-8') as f:
            f.write(resv_text)

# 入口
async def main_run(websocket):
    await echo(websocket)
    await recv_msg(websocket)


stat_sever = websockets.serve(main_run,'127.0.0.1',9999)
print('成功建立连接')
loop = asyncio.get_event_loop()
loop.run_until_complete(stat_sever)

# 保持长连接 需要不断的监听返回的数据
loop.run_forever()



