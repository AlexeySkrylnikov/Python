element_count = int(input('Введите количество элементов в списке: '))

number_list = []

i = 0
element = 0

while i < element_count:
    number_list.append(input(f'Введите значение {i}-го элемента списка: '))
    i += 1

for elem in range(int(len(number_list)/2)):
    number_list[element], number_list[element + 1] = number_list[element + 1], number_list[element]
    element += 2

print(number_list)
