# Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()),
# вычитание (__sub__()),
# умножение (__mul__()),
# деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

# Класс клетка
class Cell:

    # Конструктор
    def __init__(self, quantity):
        self.quantity = int(quantity)

    # Сложение
    def __add__(self, other):
        return f'Результат сложения равен: {self.quantity + other.quantity}'

    # Вычитание
    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Результат сложения равен: {self.quantity - other.quantity}'

    # Умножение
    def __mul__(self, other):
        return f'Результат умножения равен: {self.quantity * other.quantity}'

    # Деление
    def __truediv__(self, other):
        return f'Результат деления равен: {self.quantity // other.quantity}'

    # Организация ячеек по рядам
    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell_1 = Cell(21)
cell_2 = Cell(2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(7))
