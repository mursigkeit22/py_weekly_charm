import asyncio


# 1: Coroutines don’t do much on their own until they are tied to the event loop
async def main():
    print("Hello ...")
    await asyncio.sleep(1)
    print("World!")


main()
print("========================")
asyncio.run(main())
