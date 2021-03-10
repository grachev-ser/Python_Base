# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class MyException(Exception):
    # Конструктор
    def __init__(self, txt):
        self.txt = txt


try:
    input_1 = int(input('Введите числитель: '))
    input_2 = int(input('Введите знаменатель: '))
    if input_2 == 0:
        raise MyException("Деление на ноль!")
    else:
        print(input_1 / input_2)
except ValueError:
    print("Введите число")
except MyException as err:
    print(err)
