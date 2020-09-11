import asyncio
from codetiming import Timer
import requests
# request isn't asyncio library, so this code won't be asynchronous
urls = ['http://18.220.208.131/capacity/', 'http://18.220.208.131/capacity2/']


async def coro(link):
    response = requests.get(link)
    print(response.text)
    return response.text

with Timer():
    loop = asyncio.get_event_loop()
    tasks = [coro(urls[0]), coro(urls[1])]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()




