# The next version of the program is the same as the last,
# except for the addition of a time.sleep(delay)
# in the body of your task loop.
# This adds a delay based on the value retrieved
# from the work queue to every iteration of the task loop.
# The delay simulates the effect of a blocking call
# occurring in your task.
# A blocking call is code that stops the CPU from
# doing anything else for some period of time.
import time
import queue
from codetiming import Timer


def task(name, queue):
    timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
    while not queue.empty():
        delay = queue.get()
        print(f"Task {name} running, delay: {delay}")
        timer.start()
        time.sleep(delay)
        timer.stop() #stops the timer instance and outputs the elapsed time since timer.start() was called.
        yield


def main():
    work_queue = queue.Queue()
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    tasks = [task("One", work_queue), task("Two", work_queue)]
    done = False
    with Timer(text="\nTotal elapsed time: {:.1f}"):
        while not done:
            for t in tasks:
                try:
                    next(t)
                except StopIteration:
                    tasks.remove(t)
                if len(tasks) == 0:
                    done = True


if __name__ == "__main__":
    main()
