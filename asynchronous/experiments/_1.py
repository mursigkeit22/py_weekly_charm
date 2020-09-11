import asyncio
from codetiming import Timer
import requests
# request isn't asyncio library, so this code won't be asynchronous
urls = ['http://18.220.208.131/capacity/', 'http://18.220.208.131/capacity2/']


async def coro(link):
    response = requests.get(link)
    return response.text


async def main():
    t = asyncio.create_task(coro(urls[0]))
    t2 = asyncio.create_task(coro(urls[1]))
    for result in asyncio.as_completed((t, t2)):
        complete = await result
        print(complete)


with Timer():
    asyncio.run(main())
