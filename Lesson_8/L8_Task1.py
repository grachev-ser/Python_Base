# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

from datetime import date


class Data:

    # Конструктор
    def __init__(self, string):
        self.string = string.split('-')

    @classmethod
    def type(cls, string):
        try:
            day, month, year = [int(i) for i in string.split('-')]
            return f"{day}\n{month}\n{year}"
        except ValueError:
            return 'Указана неправильная дата!'

    @staticmethod
    def valid(string):
        try:
            day, month, year = string.split('-')
            date(int(year), int(month), int(day))
            return 'Есть такая дата!'
        except ValueError:
            return 'Указана неправильная дата!'


print(Data.valid('03-03-2015'))
print(Data.type('03-03-2021'))