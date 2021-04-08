class ComplexNumbers:
    """
    Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
    Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
    Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
    Проверьте корректность полученного результата.
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сложение z1 и z2 равно')
        return f'z1 + z2 = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z1 * z2 = {self.a * other.a - self.b * other.b} + {self.b * other.a + self.b * other.b}i'


z1 = ComplexNumbers(2, 3)
z2 = ComplexNumbers(-1, 0)
print(z1 + z2)
print(z1 * z2)
