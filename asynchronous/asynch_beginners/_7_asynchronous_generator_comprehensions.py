import asyncio
# neither asynchronous generators nor comprehensions make the iteration concurrent.
# All that they do is provide the look-and-feel of their synchronous counterparts, but with the ability
# for the loop in question to give up control to the event loop for some other coroutine to run.


# In other words, asynchronous iterators and asynchronous generators
# are not designed to concurrently map some function over a sequence or iterator.
# They’re merely designed to let the enclosing coroutine allow other tasks to take their turn.
# asynchronous generator
async def mygen(u: int = 10):
    i = 0
    while i < u:
        yield 2 ** i
        i += 1
        await asyncio.sleep(0.1)


# asynchronous comprehension
async def main():
    # The async for and async with statements are only needed to the extent that
    # using plain for or with would “break” the nature of await in the coroutine.
    g = [i async for i in mygen()]
    f = [j async for j in mygen() if not (j // 3 % 5)]
    return g, f


g, f = asyncio.run(main())
print(g)
print(f)

# for j in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]:
#     print(j, not (j // 3 % 5))
