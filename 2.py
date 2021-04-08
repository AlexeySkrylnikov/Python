class DivByZeroExp(Exception):
    """
    Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
    Проверьте его работу на данных, вводимых пользователем.
    При вводе нуля в качестве делителя программа должна корректно
    обработать эту ситуацию и не завершиться с ошибкой.
    """
    pass


try:
    num_1 = float(input('Введите делимое: '))
    num_2 = float(input('Введите делитель: '))

    if num_2 != 0:
        res = num_1 / num_2
        print(res)
    else:
        raise DivByZeroExp
except DivByZeroExp:
    print('Ошибка! Деление на ноль!')
except ValueError:
    print('Ошибка в значении!')
