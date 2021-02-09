# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

products = []
while input("Вы хотите добавить товар? Введите да или нет: ") == 'да':
    num = int(input("Введите номер товара: "))
    features = {}
    name = input("Введите название товара: ")
    features["Название"] = name
    cost = input("Введите цену товара: ")
    features["Цена"] = cost
    quantity = input("Введите кол-во товара: ")
    features["Кол-во"] = quantity
    unit = input("Введите единицу измерения товара: ")
    features["Единицы"] = unit
    products.append(tuple([num, features]))
print(products)

analytics = {}
for product in products:
    for feature_key, feature_value in product[1].items():
        if feature_key in analytics:
            analytics[feature_key].append(feature_value)
        else:
            analytics[feature_key] = [feature_value]
print(analytics)
