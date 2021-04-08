class Date:
    """
    Реализовать класс «Дата», функция-конструктор которого должна
    принимать дату в виде строки формата «день-месяц-год».
    В рамках класса реализовать два метода. Первый,
    с декоратором @classmethod. Он должен извлекать число,
    месяц, год и преобразовывать их тип к типу «Число».
    Второй, с декоратором @staticmethod, должен проводить
    валидацию числа, месяца и года (например, месяц — от 1 до 12).
    Проверить работу полученной структуры на реальных данных.
    """

    def __init__(self, str_date):
        self.str_date = str_date

    def __str__(self):
        return f'Пользователь указал дату: {self.str_date}'

    @classmethod
    def date_values_extract(cls, str_date):
        date_list = []

        for num in str_date.split('-'):
            date_list.append(num)

        return tuple(map(int, date_list))

    @staticmethod
    def date_valid(date):
        if 1 <= date[0] <= 31:
            if 1 <= date[1] <= 12:
                # if 2021 >= date[2] >= 0:
                if 4 <= len(str(date[2])) <= 4:
                    return f'Ошибок в дате нет: {date[0]}-{date[1]}-{date[2]}'
                else:
                    return f'Неверно указан год -  {date[2]}'
            else:
                return f'Неверно указан месяц - {date[1]}'
        else:
            return f'Неверно указан день - {date[0]}'


user_date = input('Укажите дату в формате день-месяц-год (q - выход): ')

while True:
    if 'Q' != user_date != 'q':
        new_date_1 = Date(user_date)
        print(new_date_1)
        print(Date.date_valid(Date.date_values_extract(user_date)))
        user_date = input('Укажите дату в формате день-месяц-год (q - выход): ')
    else:
        break
