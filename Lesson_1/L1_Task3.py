# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# Запрос у пользователя данных
n = int(input("Введите произвольное целое число: "))
# Сумма чисел
total = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
# Вывод на экран
print("Результат расчета: " + str(total))