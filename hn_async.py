import aiohttp
import asyncio

total = 10 # maximum is about 500
url = 'https://hacker-news.firebaseio.com' # https://github.com/HackerNews/API

async def main():
    async with aiohttp.ClientSession(url) as session:
        ids = await get_json(session, '/v0/topstories.json')
        tasks = [get_json(session, f'/v0/item/{id}.json') for id in ids[:total]]
        items = await asyncio.gather(*tasks)
    
    for i, item in enumerate(items, start=1):
        if item:
            print(f"{i:2}) {item['title']} | {item.get('url')}")
            print(f"    https://news.ycombinator.com/item?id={item['id']} | {item['by']} | {item['score']}")

async def get_json(session, url):
    async with session.get(url) as r:
        return await r.json()


from time import time
s = time()
asyncio.run(main())
e = time()
print(e - s)


# total | time (sec)
#    10      0.7
#    20      0.7
#    30      0.8
#   100      0.8
#   500      1.2
