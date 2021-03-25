user_str = input('Введите текст для записи в файл: ')

while user_str != '':
    with open('1.txt', 'a', encoding='utf-8') as f_obj:
        f_obj.writelines(user_str+'\n')
    user_str = input('Введите текст для записи в файл: ')
    if user_str == '':
        break
