subjects_res = {}

with open('6.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        subject, lecture, practice, lab = line.split()
        lecture_val = lecture.split('(')[0]
        practice_val = practice.split('(')[0]
        lab_val = lab.split('(')[0]
        try:
            if lecture_val == '—':
                lecture_val = 0
            if practice_val == '—':
                practice_val = 0
            if lab_val == '—':
                lab_val = 0
            subjects_res[subject.split(':')[0]] = int(lecture_val) + int(practice_val) + int(lab_val)
        except ValueError:
            print('Ошибка значения!')
print(f'Общее количество часов по предметам: \n{subjects_res}')
