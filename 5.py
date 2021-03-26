class Stationery:
    def __init__(self, title):
        self.title = title

    def drawing(self):
        print(f'Запуск отрисовки {self.title}.')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def drawing(self):
        print(f'Метод рисования: {self.title}. Запуск отрисовки ручкой.')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def drawing(self):
        print(f'Метод рисования: {self.title}. Запуск отрисовки карандашом.')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def drawing(self):
        print(f'Метод рисования: {self.title}. Запуск отрисовки маркером.')


new_pen_draw = Pen('Ручка')
new_pencil_draw = Pencil('Карандаш')
new_handle_draw = Handle('Маркер')

new_pen_draw.drawing()
new_pencil_draw.drawing()
new_handle_draw.drawing()
