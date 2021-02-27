# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# Элементы
element_int = 1
element_float = 2.0
element_complex = complex(3, 4)
element_str = "Five"
element_list = [6, 7]
element_tuple = (8, 9)
# Список элементов
elements_list = [element_int, element_float, element_complex, element_str, element_list, element_tuple, None]
# Проверка типа данных каждого элемента
for element in elements_list:
    print(type(element))
