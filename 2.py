lines_count = 0
words_count = 0

with open('2.txt', encoding='utf-8') as f_obj:
    lines = f_obj.readlines()
    for line in lines:
        lines_count += 1
        words_count += len(line.split())
        print(f'Строка "{line.strip()}" содержит {len(line.split())} слов(а)')

print(f'Общее кол-во строк: {lines_count}')
print(f'Общее Кол-во слов: {words_count}')
