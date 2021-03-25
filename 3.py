salary = []
poor = []
amount = 0
count = 0

with open('3.txt', 'r', encoding='utf-8') as f_obj:
    salary = f_obj.read().split('\n')

for line in salary:
    line = line.split()
    try:
        if float(line[1]) > 0:
            amount += float(line[1])
            count += 1
        if float(line[1]) < 20000:
            for i in line:
                poor.append(i)
    except ValueError:
        print(f'У "{line[0]}" з.п. "{line[1]}" указана не верно!')

average = amount / count

print(f'Сумма заработной платы сотрудников: {amount}')
print(f'Средняя з.п.: {round(average,2)}')
print(f'З.п. меньше 20000 у {poor}')
