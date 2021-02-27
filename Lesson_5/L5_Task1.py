# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_list = []
while True:
    data = input("Введите данные: ")
    if data == '':
        print(my_list)
        exit()
    else:
        newline = data + '\n'
        my_list.append(newline)

    with open("L5_Task1.txt", "w") as file:
        file.writelines(my_list)
