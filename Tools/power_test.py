import httpx
import asyncio
import time


# r = httpx.get(f"https://yz.lol.qq.com/v1/zh_cn/champions/annie/index.json")
# print(r.text)

url = "http://httpbin.org/"

async def req(client,i):
    res = await client.get(url)
    print(f'第{i + 1}次请求，status_code = {res.status_code}')
    return res

async def main():
    async with httpx.AsyncClient() as client:
        task_list = []
        for i in range(10):
            res = req(client,i)
            task = asyncio.create_task(res) # 创建任务
            task_list.append(task)
            await asyncio.gather(*task_list) # 收集任务

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'异步发送300次请求，耗时：{end - start}')