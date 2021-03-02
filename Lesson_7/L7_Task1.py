# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

# Класс матрицы
class Matrix:
    # Конструктор
    def __init__(self, my_list):
        self.my_list = my_list

    # Перегрузка метода вывода на печать
    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    # Перегрузка метода добавить
    def __add__(self, other_matrix):
        for i in range(len(self.my_list)):
            for j in range(len(other_matrix.my_list[i])):
                self.my_list[i][j] += other_matrix.my_list[i][j]
        return Matrix.__str__(self)


matrix1 = Matrix([[1, 0, 1], [2, 0, 2], [3, 1, 3], [4, 1, 4]])
matrix2 = Matrix([[-1, 0, -1], [-2, 0, -2], [-3, -1, -3], [-4, 1, -4]])
print(matrix1.__add__(matrix2))