import asyncio
from codetiming import Timer

# An asynchronous program runs in a single thread of execution.
# The context switch from one section of code to another
# that would affect data is completely in your control.


async def task(name, work_queue):
    timer = Timer()
    while not work_queue.empty():
        delay = await work_queue.get()
        print(f"Task {name} running")
        timer.start()
        await asyncio.sleep(delay) #This creates a non-blocking delay
        # that will perform a context switch back to the caller main()
        timer.stop()

# await asyncio.sleep(delay) is non-blocking in regards to the CPU.
# Instead of waiting for the delay to timeout,
# the CPU registers a sleep event on the event loop task queue and
# performs a context switch by passing control to the event loop.
# The event loop continuously looks for completed events and
# passes control back to the task waiting for that event.


async def main():
    work_queue = asyncio.Queue()
    for work in [15, 5, 10, 2]:
        await work_queue.put(work)
    with Timer():
        await asyncio.gather( #Create two tasks based on task()
            # and start running them. Wait for both of these to be completed
            # before moving forward.
            asyncio.create_task(task("One", work_queue)),
            asyncio.create_task(task("Two", work_queue)),
        )

if __name__ == "__main__":
    asyncio.run(main()) #This creates what’s known as an event loop
    # The event loop is at the heart of the Python async system.
    # It runs all the code, including main(). When task code is executing,
    # the CPU is busy doing work. When the await keyword is reached,
    # a context switch occurs, and control passes back to the event loop.
    # The event loop looks at all the tasks waiting for an event
    # (in this case, an asyncio.sleep(delay) timeout)
    # and passes control to a task with an event that’s ready.