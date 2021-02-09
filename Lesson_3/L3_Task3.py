# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    # Список аргументов
    list_arg = [x, y, z]
    # Минимальный аргумент
    min_element = min(list_arg)
    # Удаляем минимальынй аргумент
    list_arg.remove(min_element)
    print(sum(list_arg))


my_func(-4, 2, 1)