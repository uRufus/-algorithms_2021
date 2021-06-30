"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
import timeit
from collections import OrderedDict
# Создание словарей
test_order_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
test_dict = {'a': 1, 'b': 2, 'c': 3}
print("Замер скорости при создании OrderedDict с элементами")
print(timeit.timeit("test_order_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])", globals=globals()))
print("Замер скорости при создании Dict с элементами")
print(timeit.timeit("test_dict = {'a': 1, 'b': 2, 'c': 3}", globals=globals()))


print("Замер скорости при добавлении элемента в OrderedDict")
print(timeit.timeit("test_order_dict['d'] = 4", globals=globals()))
print("Замер скорости при добавлении элемента в Dict")
print(timeit.timeit("test_dict['d'] = 4", globals=globals()))

print("Замер скорости при выборе элемента в OrderedDict")
print(timeit.timeit("test_order_dict['a']", globals=globals()))
print("Замер скорости при выборе элемента в Dict")
print(timeit.timeit("test_dict['a']", globals=globals()))

'''
Создание словаря с элементами происходит намного быстрее, чем при использовании OrderedDict.
Добавление элемента в словарь происходит немного быстрее, чем при использовании OrderedDict.
Выбор элемента из словаря происходит практически с такой же скоростью, как и в OrderedDict.
При учете выводов выше, нет необходимости использовать OrderedDict в Python 3.6 и более поздних версиях
'''
