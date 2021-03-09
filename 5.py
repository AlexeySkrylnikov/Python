profit = float(input('Specify profit: '))  # выручка
costs = float(input('Specify costs: '))  # издержки

different = profit - costs  # прибыль

# print(different)

if different > 0:
    print(f'Компания работает с прибылью: {different}')
    print(f'Рентабельность составила: {different / profit}')
    workers_count = int(input('Укажите кол-во работников в компании: '))
    print(f'Прибыль на каждого сотрудника составила: {different / workers_count}')
else:
    print(f'Прибыль отсутствует: {different}')
