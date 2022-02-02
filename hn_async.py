import aiohttp
import asyncio

total = 10
url = 'https://hacker-news.firebaseio.com'

async def main():
    async with aiohttp.ClientSession(url) as session:
        async with session.get('/v0/topstories.json') as r:
            ids = await r.json()

        tasks = [task(session, f'/v0/item/{id}.json') for id in ids[:total]]
        items = await asyncio.gather(*tasks)
    
    for i, item in enumerate(items, start=1):
        if item:
            print(f"{i:2}) {item['title']} | {item.get('url')}")
            print(f"    https://news.ycombinator.com/item?id={item['id']} | {item['by']} | {item['score']}")

async def task(session, url):
    async with session.get(url) as r:
        return await r.json()


from time import time
s = time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
e = time()
print(e - s)


# total | time (sec)
#    10      0.7
#    20      0.7
#    30      0.8
#   100      0.8
#   500      1.2