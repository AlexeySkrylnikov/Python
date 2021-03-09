number = int(input('Specify number: '))
maximum = number % 10  # остаток от деления
number = number // 10  # целочисленноеделение
while number > 0:
    if number % 10 > maximum:
        maximum = number % 10
    number = number // 10
print(f'Max number is {maximum}')
