from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, clothe_param):
        self.clothe_param = clothe_param

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        res = round((self.clothe_param / 6.5 + 0.5), 2)
        return res


class Suit(Clothes):
    
    @property
    def calculate(self):
        res = round((2 * self.clothe_param + 0.3))
        return res


new_coat_1 = Coat(46)
new_suit_1 = Suit(150)

print('Расход ткани на костюм составит:', new_suit_1.calculate)
print('Расход ткани на пальто составит:', new_coat_1.calculate)
print('Общий расход ткани составит:', new_coat_1.calculate + new_suit_1.calculate)
