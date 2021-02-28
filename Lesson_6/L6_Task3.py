# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

# Класс работник
class Worker:
    # Конструктор
    def __init__(self, name, surname, position, wage, bonus):
        # Имя
        self.name = name
        # Фамилия
        self.surname = surname
        # Должность
        self.position = position
        # Доход
        self._income = {"wage": int(wage), "bonus": int(bonus)}


# Класс должность
class Position(Worker):

    # Конструктор
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    # Возвращает полное имя сотрудника
    def get_full_name(self):
        return self.name + ' ' + self.surname

    # Возвращает доход с учетом премии
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


obj = Position('Иван', 'Иванов', 'Инженер', '100000', '20000')
print(obj.get_full_name(), obj.get_total_income())
