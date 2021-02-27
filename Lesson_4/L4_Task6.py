# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count
from itertools import cycle
from sys import argv

name, start_point = argv
for el in count(int(start_point)):
    print(el)

my_list = [False, 1, 'Test', None]
for el in cycle(my_list):
    print(el)
