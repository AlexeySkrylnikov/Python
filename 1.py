from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        red_sleep_sec = 7
        yellow_sleep_sec = 2
        green_sleep_sec = 10

        for i in cycle(self.__color):
            if i == 'Красный':
                print(i)
                sleep(red_sleep_sec)
            if i == 'Желтый':
                print(i)
                sleep(yellow_sleep_sec)
            if i == 'Зеленый':
                print(i, '\n')
                sleep(green_sleep_sec)


color_list = ['Красный', 'Желтый', 'Зеленый']
my_traffic_light = TrafficLight(color_list)
my_traffic_light.running()
