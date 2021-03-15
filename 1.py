def division_func(a, b):
    """функция деления двух чисел

    :param a: число
    :param b: число
    :return: результат деления

    """

    try:
        result = a / b
    except ZeroDivisionError:
        result = 'Деление на ноль!'
    return result


print('Результат:', division_func(10, 3))
