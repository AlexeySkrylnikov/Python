from math import factorial
from itertools import count


def fact(nums):
    elem_list = []
    for n in count(1):
        elem_list.append(n)
        if n == nums:
            break
    print('Факториал чисел:', elem_list)
    yield factorial(nums)


num = int(input('Введите число для вычесления факториала: '))

for el in fact(num):
    print('Равен:', el)
