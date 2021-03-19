from itertools import count, cycle

print('Итератор генерирующий целые числа начиная с 3 и заканчивая 10: ')
for i in count(3):
    print(i)
    if i == 10:
        break

city_list = ['Moscow', 'Milan', 'Oslo']

print('\nИтератор списка: ', city_list)

c = 0
a = 0
for i in cycle(city_list):
    if c in (0, 3, 6):
        a += 1
        print('Шаг', a)
    print(i)
    c += 1
    if c == 9:
        break
