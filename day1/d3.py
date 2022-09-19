import aiohttp
import asyncio
import requests
async def download_image(session, url):
    print('发送请求: ', url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        file_name = url.rsplit('/')[-1]
        with open(file_name, mode='wb') as f:
            f.write(content)

async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            'http://pic.bizhi360.com/bbpic/98/10798.jpg',
            'http://pic.bizhi360.com/bbpic/92/10792.jpg',
            'http://pic.bizhi360.com/bbpic/86/10386.jpg'
        ]
        tasks = [asyncio.create_task(download_image(session, url)) for url in url_list]
        await asyncio.wait(tasks)
        # task = []
        # for url in url_list:
        #     task.append(asyncio.create_task(download_image(session, url)))
        # await asyncio.wait(task)
if __name__ == '__main__':
    asyncio.run(main())