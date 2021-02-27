# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

try:
    with open('L5_Task5.txt', 'w+') as my_file:
        line = input('Введите цифры через пробел \n')
        my_file.writelines(line)
        my_numbers = line.split()
        print(sum(map(int, my_numbers)))
except IOError:
    print('Ошибка в файле')
except ValueError:
    print('Неправильно набран номер. Ошибка ввода-вывода')
