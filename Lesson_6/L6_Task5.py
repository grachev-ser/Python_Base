# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

# Базовый класс канцелярская принадлежность
class Stationery:
    # Конструктор
    def __init__(self, title):
        self.title = title

    # Рисовать
    def draw(self):
        return f'Запуск отрисовки'


# Класс ручка
class Pen(Stationery):
    # Рисовать
    def draw(self):
        return f'Запуск отрисовки {self.title}'


# Класс карандаш
class Pencil(Stationery):
    # Рисовать
    def draw(self):
        return f'Запуск отрисовки {self.title}'


# Класс маркер
class Handle(Stationery):
    # Рисовать
    def draw(self):
        return f'Запуск отрисовки {self.title}'


obj_pen = Pen('ручка')
print(obj_pen.draw())
obj_pencil = Pencil('карандаш')
print(obj_pencil.draw())
obj_handle = Handle('маркер')
print(obj_handle.draw())
