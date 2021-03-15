def sum_my_numbers():
    res = 0
    ext = False
    while ext is False:
        num = input('Введите числа через пробел (укажите Q для выхода): ').split()
        for item in num:
            if item.isdigit():
                res += int(item)

            elif item == 'q' or item == 'Q':
                ext = True
            else:
                print('Вводите только числа через пробел, для выхода укажите Q!')
        print('Сумма:', res)


sum_my_numbers()
