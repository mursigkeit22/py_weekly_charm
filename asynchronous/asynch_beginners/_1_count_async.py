import asyncio
import codetiming
import time


# A coroutine is a specialized version of a Python generator function:
# a function that can suspend its execution before reaching return,
# and it can indirectly pass control to another coroutine for some time.

async def count(name):
    print(f"One {name}")
    await asyncio.sleep(1)  # The keyword await passes function control back to the event loop.
    # (It suspends the execution of the surrounding coroutine.)

    # time.sleep(1) # won't be asynch, will take 3 seconds
    print(f"Two {name}")


async def main():
    tasks = [count(i) for i in ["a", "b", "c"]]
    await asyncio.gather(*tasks)

#     when you use await f(), it’s required that f() be an object that is awaitable.
#      an awaitable object is either
#      (1) another coroutine or
#     (2) an object defining an .__await__() dunder method that returns an iterator.


if __name__ == "__main__":
    with codetiming.Timer():
        asyncio.run(main())
