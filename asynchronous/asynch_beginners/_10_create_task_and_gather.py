import asyncio


async def coro(seq) -> list:
    await asyncio.sleep(max(seq))
    print(f"seq: {seq}")
    return list(reversed(seq))


async def main():
    #     There’s a subtlety to this pattern: if you don’t await t within main(),
    #     it may finish before main() itself signals that it is complete.
    #     Because asyncio.run(main()) calls loop.run_until_complete(main()),
    #     the event loop is only concerned (without await t present) that main() is done,
    #     not that the tasks that get created within main() are done.
    #     Without await t, the loop’s other tasks will be cancelled, possibly before they are completed.

    t = asyncio.create_task(coro([2, 3, 4]))
    b = [asyncio.create_task(coro([2, 3, 4])),
         asyncio.create_task(coro([1, 2]))]  # add to the second task number 6 and see: it won't be done
    await t
    print("t is done")
    print(f't: type {type(t)}')
    print(f't done: {t.done()}')

async def main1():
    t = asyncio.create_task(coro([2, 3, 4]))
    b = asyncio.create_task(coro([2, 3, 1]))
    v = asyncio.create_task(coro([2, 3, 5]))
    await asyncio.gather(t, b, v) # gathering all the tasks so every one would be completed
# gather() is meant to neatly put a collection of coroutines (futures) into a single future.
# As a result, it returns a single future object, and,
# if you await asyncio.gather() and specify multiple tasks or coroutines, you’re waiting for all of them to be completed.

asyncio.run(main1())
