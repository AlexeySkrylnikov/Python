class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник: {self.surname} {self.name}')

    def get_total_income(self):
        wage, bonus = self._income
        res = float(wage) + float(bonus)
        return res


w_name = input('Укажите имя сотрудника: ')
w_surname = input('Укажите фамилию сотрудника: ')
w_position = input('Укажите должность: ')
w_wage = float(input('Зар. плата: '))
w_bonus = float(input('Премия: '))

new_position = Position(w_name, w_surname, w_position, [w_wage, w_bonus])
new_position.get_full_name()
print('Доход сотрудника составит:', new_position.get_total_income())
