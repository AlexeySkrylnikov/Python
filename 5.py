with open('5.txt', 'w') as f_obj:
    try:
        nums_str = input('Введите числа через пробел: ')
        f_obj.writelines(nums_str)
        nums_int = [int(item) for item in nums_str.split()]
        amount = sum(nums_int)
        print('Сумма значений = ', amount)
    except ValueError:
        print('Ошибка в значении!')
