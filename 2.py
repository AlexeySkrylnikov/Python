old_list = [500, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [elements for numbers, elements in enumerate(old_list) if old_list[numbers] > old_list[numbers-1]]

print('Старый список: ', old_list, '\nНовый список: ', new_list)
