from itertools import cycle


def endless():
    """Yields 9, 8, 7, 6, 9, 8, 7, 6, ... forever"""
    yield from cycle((9, 8, 7, 6))


e = endless()
# for i in e:
#     print(i)


total = 0
for i in e:
    if total < 50:
        print(i, end=" ")
        total += i
    else:
        print()
        # Pause execution. We can resume later.
        break
print(next(e), next(e), next(e))
