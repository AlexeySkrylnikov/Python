class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Скорость авто {speed}, цвет {color}, это полиция? {is_police}')

    def go(self):
        print(f'{self.name} поехала!')

    def stop(self):
        print(f'{self.name} остановилась!')

    def turn(self, direction):
        print(f'{self.name} повернула на', direction)

    def show_speed(self):
        print(f'Текущая скорость {self.name}:', self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Городская машина {self.name}\n')

    def show_speed(self):
        print(f'Текущая скорость {self.name}', self.speed)
        if self.speed > 60:
            print(f'Внимание! Привышение скорости для городской машины {self.name}!')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Рабочая машина {self.name}\n')

    def show_speed(self):
        print(f'Текущая скорость {self.name}:', self.speed)
        if self.speed > 40:
            print(f'Внимание! Привышение скорости для рабочей машины {self.name}!\n')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Спорткар {self.name}\n')


class PoliceCar(Car):
    pass


Nissan = TownCar(70, 'Red', 'Nissan', False)
Gazel = WorkCar(30, 'White', 'Gazel', False)
Ferrari = SportCar(100, 'Yellow', 'Ferrari', False)
Nissan.turn('лево')
Gazel.turn('право')
Gazel.go()
Nissan.stop()
Ferrari.go()
Ferrari.show_speed()
Gazel.show_speed()
Nissan.show_speed()
