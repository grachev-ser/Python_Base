# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение экземпляров.
# Проверьте корректность полученного результата.

# Класс «Комплексное число»
class Complex:

    # Конструктор
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Сложение
    def __add__(self, other):
        return f'Сумма равна: {self.a + other.a} + {self.b + other.b} * i'

    # Умножение
    def __mul__(self, other):
        return f'Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


c_1 = Complex(2, -2)
c_2 = Complex(3, 3)
print(c_1 + c_2)
print(c_1 * c_2)
