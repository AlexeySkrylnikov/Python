def my_func(a, b, c):
    numbers = [a, b, c]
    numbers.pop(numbers.index(min(numbers)))
    return numbers


print(my_func(100, 2, 300))
