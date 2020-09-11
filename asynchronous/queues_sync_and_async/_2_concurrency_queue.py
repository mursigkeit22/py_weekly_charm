import queue


def task(name, work_queue):
    while not work_queue.empty():
        count = work_queue.get()
        total = 0
        print(f"Task {name} running, work count: {count}")
        for x in range(count):
            total += 1
            print(f"Task {name} current total: {total}")
            yield
        print(f"Task {name} total: {total}")


def main():
    work_queue = queue.Queue()
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    tasks = [task("One", work_queue), task("Two", work_queue)]
    done = False
    while not done:
        for t in tasks:
            # time.sleep(1)
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True


if __name__ == "__main__":
    main()
