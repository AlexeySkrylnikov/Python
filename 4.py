rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file_content = []
with open('4.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        new_line = line.split(' ', 1)
        new_file_content.append(rus[new_line[0]] + ' ' + new_line[1])

with open('4_new.txt', 'w', encoding='utf-8') as new_f_obj:
    new_f_obj.writelines(new_file_content)
