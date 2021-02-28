# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

# Базовый класс машина
class Car:

    # Конструктор
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    # Поехать
    def go(self):
        return f'{self.name} поехала.'

    # Остановиться
    def stop(self):
        return f'\n{self.name} остановился.'

    # Повернуть
    def turn(self, direction):
        return f'\n{self.name} повернула {direction}'

    # Возвращает текущую скорость автомобиля
    def show_speed(self):
        return f'\nСкорость: {self.speed}'


# Класс городская машина
class TownCar(Car):
    # Возвращает скорость
    def show_speed(self):
        if self.speed > 60:
            return f'\nПревышение скорости! Скорость: {self.speed}'
        else:
            return f'Скорость {self.name} в норме'


# Класс спортивная машина
class SportCar(Car):
    pass


# Класс рабочая машина
class WorkCar(Car):
    # Возвращает скорость
    def show_speed(self):
        if self.speed > 40:
            return f'\nПревышение скорости! Скорость: {self.speed}'
        else:
            return f'Скорость {self.name} в норме'


# Класс полицейская машина
class PoliceCar(Car):
    pass


town_car = TownCar('Лада', 70, 'синий', False)
print('TownCar:\n' + town_car.go(), town_car.show_speed(), town_car.turn('налево'), town_car.stop())

sport_car = SportCar('Ягуар', 170, 'красный', False)
print('SportCar:\n' + sport_car.go(), sport_car.show_speed(), sport_car.turn('направо'), sport_car.stop())

work_car = WorkCar('Камаз', 30, 'красный', False)
print('WorkCar:\n' + work_car.go(), work_car.show_speed(), work_car.turn('налево'), work_car.stop())

police_car = PoliceCar('УАЗ', 100, 'синий', True)
print('PoliceCar:\n' + police_car.go(), police_car.show_speed(), police_car.turn('направо'), police_car.stop())
