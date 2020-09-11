import concurrent.futures

counter = 0


def increment_counter(fake_value):
    global counter
    for _ in range(100):
        counter += 1

# Because the operating system knows nothing about your code and can swap threads at any point in the execution,
# it’s possible for this swap to happen after a thread has read the value but before it has had the chance to write
# it back.
# As you can imagine, hitting this exact situation is fairly rare.
# You can run this program thousands of times and never see the problem.


if __name__ == "__main__":
    fake_data = [x for x in range(5000)]
    counter = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=5000) as executor:
        executor.map(increment_counter, fake_data)

print(counter)
