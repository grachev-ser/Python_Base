# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(arg1, arg2):
    try:
        result = int(arg1) / int(arg2)
        return result
    except ZeroDivisionError:
        return print("Деление на ноль невозможно!")
    except ValueError:
        return print("Один из аргументов - не число!")


input_arg1 = input("Введите первое число: ")
input_arg2 = input("Введите второе число: ")
print(division(input_arg1, input_arg2))
