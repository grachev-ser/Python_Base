# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_data(name, surname, birth_year, city, email, phone) -> object:
    print(name, surname, birth_year, city, email, phone)


user_data(name='Ivan', surname='Ivanov', birth_year=1990, city='Moscow', email='Ivanov_i@mail.ru', phone='89265055500')
