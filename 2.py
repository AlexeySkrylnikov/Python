def users_param(first_name, last_name, birthday_year, email, phone):
    result_func = 'Фамилия: ' + first_name + ' Имя: ' + last_name + ' Год рождения: ' + birthday_year\
             + ' email: ' + email + ' Телефон: ' + phone
    return result_func


result = users_param(first_name='Иванов', birthday_year='1989', last_name='Иван', email='email@mail.ru',
                     phone='+71234567890')
print(result)
