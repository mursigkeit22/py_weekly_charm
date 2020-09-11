import asyncio


async def coro(seq) -> list:
    await asyncio.sleep(max(seq))
    print(f"seq: {seq}")
    return list(reversed(seq))


# you can loop over asyncio.as_completed() to get tasks as they are completed,
# in the order of completion.
# The function returns an iterator that yields tasks as they finish.

async def main():
    t = asyncio.create_task(coro([2, 3, 1]))
    t2 = asyncio.create_task(coro([6, 5, 0]))
    for result in asyncio.as_completed((t, t2)):
        complete = await result
        print(complete)


asyncio.run(main())
