import requests

total = 10 # maximum is about 500
url = 'https://hacker-news.firebaseio.com' # https://github.com/HackerNews/API

def main():
    with requests.Session() as session:
        ids = session.get(f'{url}/v0/topstories.json').json()
        for i, id in enumerate(ids[:total], start=1):
            item = session.get(f'{url}/v0/item/{id}.json').json()
            if item:
                print(f"{i:2}) {item['title']} | {item.get('url')}")
                print(f"    https://news.ycombinator.com/item?id={item['id']} | {item['by']} | {item['score']}")


from time import time
s = time()
main()
e = time()
print(e - s)


# total | time (sec)
#    10      1
#    20      2
#    30      3
#   100      8
#   500     40
