numbers_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list = [x for x in numbers_list if numbers_list.count(x) < 2]

print(my_list)
