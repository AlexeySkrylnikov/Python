class OrganicCell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        res = self.quantity + other.quantity
        return f'{res * "*"}'

    def __sub__(self, other):
        res = self.quantity - other.quantity
        if res < 0:
            res = 'Разность кол-ва ячеек должна быть больше нуля!'
        else:
            res = f'{res * "*"}'
        return res

    def __mul__(self, other):
        res = self.quantity * other.quantity
        return f'{res * "*"}'

    def __truediv__(self, other):
        res = self.quantity // other.quantity
        if res == 0:
            res = '0'
        else:
            res = f'{res * "*"}'
        return res

    def make_order(self, cell_in_row):
        row = ''
        for i in range(int(self.quantity / cell_in_row)):
            row += f'{"*" * cell_in_row}\\n'
        row += f'{"*" * (self.quantity % cell_in_row)}'
        return row


new_oc_1 = OrganicCell(10)
new_oc_2 = OrganicCell(5)
new_oc_3 = OrganicCell(20)
new_oc_4 = OrganicCell(2)

print('Сложение двух клеток =', new_oc_1 + new_oc_2)
print('Вычитание двух клеток =', new_oc_1 - new_oc_2)
print('Вычитание двух клеток =', new_oc_1 - new_oc_3)
print('Умножение двух клеток =', new_oc_2 * new_oc_4)
print('Деление двух клеток =', new_oc_1 / new_oc_4)
print('Сортировка = ', new_oc_3.make_order(7))
print('Сортировка = ', new_oc_1.make_order(2))
