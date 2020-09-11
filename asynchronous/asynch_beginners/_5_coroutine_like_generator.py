

async def stuff():
    return 0x10, 0x20, 0x30


async def func():
    s = await stuff()
    print(s)
    # return s


print(func())  # Calling a coroutine in isolation returns a coroutine object: <coroutine object func at 0x02FE49E8>


###asyncio.run(func())

# similar to this:
def gen():
    yield 0x10, 0x20, 0x30


print(gen())

print(next(gen()))
