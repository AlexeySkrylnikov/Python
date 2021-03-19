from functools import reduce

numbers_list = [x for x in range(100, 1001) if x % 2 == 0]

print('Список четных числе в диапазоне от 100 до 1000', numbers_list)

print('Произведение всех чисел списка', reduce(lambda x, y: x * y, numbers_list))
