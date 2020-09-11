import asyncio
import random
from codetiming import Timer
import sys


async def part1(n: str) -> str:
    i = random.randint(0, 10)
    print(f"part1({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result {n}- part1"
    print(f"Returning part1({n}) result: {result}.")
    return result


async def part2(n: str, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"part2 {n, arg} sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result {n}-part2 derived from {arg}"
    print(f"Returning part2 {n, arg} result: {result}.")
    return result


async def chain(n: str) -> None:
    with Timer() as t:
        p1 = await part1(n)
        p2 = await part2(n, p1)
    print(f"-->Chained result {n} => {p2} (took {t.last:0.2f} seconds).")


async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))


if __name__ == "__main__":
    random.seed(444)
    print("sys.argv: ", sys.argv, len(sys.argv))
    args = ["a", "b", "c"] if len(sys.argv) == 1 else sys.argv[1:]
    with Timer(text="Programm finished in {:.2f} seconds"):
        asyncio.run(main(*args))
