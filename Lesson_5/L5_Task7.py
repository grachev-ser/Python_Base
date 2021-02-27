# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

from json import dumps

SRC_FILENAME = "L5_Task7.txt"
DST_FILENAME = "L5_Task7.json"
results = [{}, {}]

try:
    with open(SRC_FILENAME, encoding='utf-8') as my_file:
        lines = my_file.readlines()

    for line in lines:
        name, comp_type, proceeds, expenses = line.split()
        results[0][name] = int(proceeds) - int(expenses)

    results[1]['average_profit'] = round(sum(profit for comp_type, profit in results[0].items() if profit > 0) /
                                         len(results[0]))

    print(results)

    with open(DST_FILENAME, "w", encoding='utf-8') as my_json_file:
        my_json_file.write(dumps(results))
except IOError as e:
    print(e)
except ValueError:
    print("Некорректные данные")
