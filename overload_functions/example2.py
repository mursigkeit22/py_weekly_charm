from overload_functions import overload
import math


@overload
def area(l, b):
    return l * b


@overload
def area(r):
    return math.pi * r ** 2


def qua(m, n, s):  # без overload можно написать функцию с новым названием, но нельзя написать area - она будет перехватывать все вызовы
    return m ** 2

# @overload          # как и полагается питону, если эту функцию раскомментить, она перехватит вызовы у функции  def area(l, b):return l * b
# def area(m,n):
#     return m+n


print(area(3, 4))
print(area(7))
# print(area(1, 2, 3))  # Exception: no matching function found
