def my_func(x, y):
    i = 1
    res = x
    while i < abs(y):
        res *= x
        i += 1
    if y < 0:
        res = 1 / res
    return res


def my_func_2(x, y):
    result_func = x ** y
    return result_func


print(my_func(2, -4))
print(my_func_2(2, -4))
