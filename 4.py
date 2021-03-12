user_str = input('Введите текст: ')  # qweasdzxcR1234 sdcxz 1234567890pQWE

allowed_len = 10

for num, elem in enumerate(user_str.split()):
    if len(elem) > allowed_len:
        elem = elem[:allowed_len]
    print(f'{num} {elem} (len = {len(elem)})')
