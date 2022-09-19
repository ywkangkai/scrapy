import asyncio

import asyncio
async def others():
    print('start')
    await asyncio.sleep(2)
    print('end')
    return '这是执行完协程函数后所得到的结果'


async def func():
    print('执行协程函数内部代码')
    response = await others()
    print(response)


asyncio.run(func())