# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них

# Набор натуральных чисел
my_list = [7, 5, 3, 3, 2]


def element_placement(num_list, num):
    # Максимальное число в списке
    max_num = max(num_list)
    if num > max_num:
        # Добавляем вначало
        num_list.insert(0, num)
    elif num in num_list:
        value_index = num_list.index(num)
        num_list.insert(value_index, num)
    else:
        # Добавляем вконец
        num_list.append(num)


while input("Вы хотите новый элемент рейтинга? Введите да или нет: ") == 'да':
    while True:
        # Пользователь вводит месяц в виде целого числа от 1 до 12.
        value_input = input("Введите целое число: ")
        try:
            # Пробуем перевести в число, если не удается переходим в except
            value = int(value_input)
            element_placement(my_list, value)
            print(my_list)
            break
        except ValueError:
            print("Данные введены неверно!")
