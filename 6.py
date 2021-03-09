start = float(input('Укажите стартовое значение: '))
wants = float(input('Укажите желаемое расстояние: '))

day = 1

while start <= wants:
    print(f'День {day}: {start:.2f}')
    start += start * 0.1
    day += 1

print(f'День {day}: {start:.2f}')
print(f'На {day} день Вы достигните результата не менее {wants} км.')
