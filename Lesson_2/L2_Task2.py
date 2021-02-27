# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# Элементы
element1_int = input("Введите целое число: ")
element2_float = input("Введите вещественное число: ")
element3_int = input("Введите целое число: ")
element4_float = input("Введите вещественное число: ")
element5_str = input("Введите строку: ")
# Список элементов
elements_list = [element1_int, element2_float, element3_int, element4_float, element5_str]
print(elements_list)

num = 0
# Обмен значений соседних элементов
while num < len(elements_list):
    if (num + 1) < len(elements_list):
        temp = elements_list[num]
        elements_list[num] = elements_list[num + 1]
        elements_list[num + 1] = temp
        num += 2
    else:
        num += 2

print(elements_list)
