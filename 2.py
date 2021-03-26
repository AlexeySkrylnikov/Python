class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_of_asphalt(self):
        res = self._length * self._width * 25 * 5
        return res


road_length = float(input('Укажите длину дороги: '))
road_width = float(input('Укажите ширину дороги: '))
new_road = Road(road_length, road_width)
print(f'Потребуется:', new_road.weight_of_asphalt(), 'тонн асфальта')
