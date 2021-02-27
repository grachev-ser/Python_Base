# Создать текстовый файл (не программно).
# Сохранить в нем несколько строк.
# Выполнить подсчет количества строк, количества слов в каждой строке.


with open("L5_Task2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in line")
    print(f"String count is {lines}")