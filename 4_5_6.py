# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В
# классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
#
# Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
# подходящую структуру (например, словарь).
#
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class OfficeEquipmentStorage:
    def __init__(self):
        self._storage_list = []

    def add_to_storage(self, office_equipment):
        self._storage_list.append(office_equipment)

    def __str__(self):
        return f'Склад: {self._storage_list}'

    def __len__(self):
        return len(self._storage_list)


class OfficeEquipment:
    def __init__(self, name, manufacture, model, price, quantity, article_number):
        self.name = name
        self.manufacture = manufacture
        self.model = model
        self.price = price
        self.quantity = quantity
        self.article_number = article_number


class Printer(OfficeEquipment):
    def __init__(self, name, manufacture, model, price, quantity, article_number, type_of_printer):
        super().__init__(name, manufacture, model, price, quantity, article_number)
        self.type_of_printer = type_of_printer
        self.printer_dict = {'Название техники': self.name, 'Производитель': self.manufacture, 'Название': self.model,
                             'Цена': self.price, 'Количество на складе': self.quantity,
                             'Артикул': self.article_number, 'Тип': self.type_of_printer}

    def __repr__(self):
        return f'{self.printer_dict}'

    @staticmethod
    def action():
        return 'Принтер внесен на склад!'


class Copier(OfficeEquipment):
    def __init__(self, name, manufacture, model, price, quantity, article_number, scaling_up):
        super().__init__(name, manufacture, model, price, quantity, article_number)
        self.scaling_up = scaling_up
        self.copier_dict = {'Название техники': self.name, 'Производитель': self.manufacture, 'Название': self.model,
                            'Цена': self.price, 'Количество на складе': self.quantity,
                            'Артикул': self.article_number, 'Масштабирование': self.scaling_up}

    def __repr__(self):
        return f'{self.copier_dict}'

    @staticmethod
    def action():
        return 'Копир внесен на склад!'


class Scanner(OfficeEquipment):
    def __init__(self, name, manufacture, model, price, quantity, article_number, type_of_scanner):
        super().__init__(name, manufacture, model, price, quantity, article_number)
        self.type_of_scanner = type_of_scanner
        self.scanner_dict = {'Название техники': self.name, 'Производитель': self.manufacture, 'Название': self.model,
                             'Цена': self.price, 'Количество на складе': self.quantity,
                             'Артикул': self.article_number, 'Тип сканера': self.type_of_scanner}

    def __repr__(self):
        return f'{self.scanner_dict}'

    @staticmethod
    def action():
        return 'Сканер внесен на склад!'


storage = OfficeEquipmentStorage()

while True:
    try:
        value = int(input('Укажите цифру для ввода данных о технике\n1 - принтер\n2 - сканер\n3 - копир\n'
                          '4 - показать склад\n'
                          '0 - выход: '))
        if value != 0:
            if value == 4:
                if len(storage) == 0:
                    print('Склад пустой!')
                else:
                    print(storage)
            else:
                manufacture = input('Укажите производителя: ')
                model = input('Укажите модель: ')
                price = float(input('Укажите цену: '))
                quantity = int(input('Укажите кол-во на складе: '))
                article_number = input('Укажите артикул: ')
                if value == 1:
                    type_of_printer = int(input('Укажите тип принтера (0 - струйный или 1 - лазерный): '))
                    new_printer = Printer('Принтер', manufacture, model, price, quantity, article_number,
                                                   type_of_printer)
                    storage.add_to_storage(new_printer)
                    print(new_printer.action())
                if value == 2:
                    scaling_up = int(input('Укажите тип сканера (0 - планшетный, 1 - протяжный или 2 - слайд): '))
                    new_scanner = Scanner('Сканер', manufacture, model, price, quantity, article_number,
                                                   scaling_up)
                    storage.add_to_storage(new_scanner)
                    print(new_scanner.action())
                if value == 3:
                    type_of_scanner = int(input('Укажите наличие масштабируемости у копира (0 - нет, 1 - есть): '))
                    new_copier = Copier('Копир', manufacture, model, price, quantity, article_number,
                                                  type_of_scanner)
                    storage.add_to_storage(new_copier)
                    print(new_copier.action())
        else:
            if len(storage) == 0:
                print('Склад пустой!')
            else:
                print(storage)
            break
    except ValueError:
        print('Ошибка значения!')
