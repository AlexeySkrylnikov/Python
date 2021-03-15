def int_func(string):
    return string.title()


ext = False

while ext is False:
    user_str = input('Введите текст (Q - для выхода): ')
    if user_str == 'Q' or user_str == 'q':
        ext = True
    else:
        print(int_func(user_str))
