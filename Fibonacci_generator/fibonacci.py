# https://sourcery.ai/blog/effective-collection-handling/
def fib():
    yield 0
    a, b = 1, 1
    while True:
        yield b
        a, b = b, a + b


def print_fibonacci(max_size):
    for number in fib():
        if number < max_size:
            print(number)
        else:
            break


print_fibonacci(100)

# When fib() is first invoked it executes as normal until it hits the yield statement.
# It then returns control to its caller along with the value, just like return would do.
# However, fib() has only been suspended, and all its state has been saved.
# When the iterator it returns is queried again
# it resumes from where it left off instead of starting again from the beginning like a normal function.
