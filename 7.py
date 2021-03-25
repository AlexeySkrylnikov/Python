import json


cnt = 0
income_list = []
final_list = []
income_dict = {}
average_dict = {}

with open('7.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        try:
            res = float(line.split()[2]) - float(line.split()[3])
            cnt += 1
            if res > 0:
                income_list.append(res)
                income_dict[line.split()[1]+' '+line.split()[0]] = round(res, 2)
                print(f'У компании {line.split()[1]} "{line.split()[0]}" доход составил: {res:.2f}')
            else:
                print(f'У компании {line.split()[1]} "{line.split()[0]}" убытки составили: {res:.2f}')
        except ValueError:
            print(f'Внимание! Ошибка значения у фирмы "{line.split()[0]}": {line.split()[2]}, {line.split()[3]}')

average = sum(income_list) / len(income_list)
print('\nСредний доход составил: %.2f' % average)
average_dict['average_profit'] = round(average, 2)

final_list.append(income_dict)
final_list.append(average_dict)
print(f'\nРезультат программы в словаре: \n{final_list}')

with open('7.json', 'w', encoding='utf-8') as json_obj:
    json.dump(final_list, json_obj)
