import asyncio
import aiohttp
from codetiming import Timer


async def download_site(session, url):
    async with session.get(url) as response:
        print(f"Read {response.content_length} from {url}")


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)
        # Once all the tasks are created, this function uses asyncio.gather()
        # to keep the session context alive until all of the tasks have completed.


if __name__ == "__main__":
    sites = [
                "https://www.jython.org",
                "http://olympus.realpython.org/dice",
            ] * 80
    with Timer():
        asyncio.get_event_loop().run_until_complete(download_all_sites(sites))  # asyncio.run()

# run_until_complete(self, future):
# """Run the event loop until a Future is done.
#  Return the Future's result, or raise its exception.
# Futures are objects that have the __await__() method implemented, and their job is to hold a certain state and result. The state can be one of the following:
#
# PENDING - future does not have any result or exception set.
# CANCELLED - future was cancelled using fut.cancel()
# FINISHED - future was finished, either by a result set using fut.set_result() or by an exception set using fut.set_exception()