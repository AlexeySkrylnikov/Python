# month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
#               'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
#
# while True:
#     month = int(input('Укажите цифру месяца: '))
#     print(f'Это месяц: {month_list[month - 1]}') if 1 <= month <= 12 else print('Укажите цифру от 1 до 12!')

season_list = ['зима', 'весна', 'лето', 'осень']
season_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}

month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
              'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

while True:
    month = int(input('Укажите номер месяца от 1 до 12: '))
    if 1 <= month <= 12:

        month_name = month_list[month - 1]

        if month == 12 or 1 <= month <= 2:
            print(f'Список: Месяц {month_name} - {season_list[0]}')
            print(f'Словарь: Месяц {month_name} - {season_dict.get(1)}')

        elif 3 <= month <= 5:
            print(f'Список: Месяц {month_name} - {season_list[1]}')
            print(f'Словарь: Месяц {month_name} - {season_dict.get(2)}')

        elif 6 <= month <= 8:
            print(f'Список: Месяц {month_name} - {season_list[2]}')
            print(f'Словарь: Месяц {month_name} - {season_dict.get(3)}')

        else:
            print(f'Список: Месяц {month_name} - {season_list[3]}')
            print(f'Словарь: Месяц {month_name} - {season_dict.get(4)}')

    else:
        print('Укажите цифру месяца от 1 до 12!')
