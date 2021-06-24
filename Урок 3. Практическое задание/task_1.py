"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""


def check_time(func):
    import time

    def decor(*args, **kwargs):
        start_val = time.time()
        return_value = func(*args, **kwargs)
        end_val = time.time()
        print(f'Операция заняла {end_val - start_val} сек')
        return return_value
    return decor



@check_time
def fulfill_list(n):
    a = []
    for i in range(n):
        a.append(i)
    return a


@check_time
def fulfill_dict(n):
    a = {}
    for i in range(n):
        a[i] = i
    return a

@check_time
def find_element_in_list(n, el):
    if el in n:
        return n[el]

@check_time
def find_element_in_dict(n, el):
    if el in n:
        return n[el]

@check_time
def delete_element_in_list(n, el):
    if el in n:
        n.remove(el)

@check_time
def delete_element_in_dict(n, el):
    if el in n:
        del n[el]

print("Время добавления в список 30000000 значений")
l1 = fulfill_list(30000000)
print("Время добавления в словарь 30000000 значений")
d1 = fulfill_dict(30000000)
print("Список работает быстрее, так как в словаре идет хеширование при добавлении новых значений")
print("Время поиска в списке 10000 значения")
find_element_in_list(l1, 1000000)
print("Время поиска в словаре 10000 значения")
find_element_in_dict(d1, 1000000)
print("Словарь быстрее находит элемент, так как он захештрован")
print("Время удаления элемента в списке 10000 значения")
delete_element_in_list(l1, 1000000)
print("Время удаления элемента в словаре 10000 значения")
delete_element_in_dict(d1, 1000000)
print("Словарь быстрее удаляет элемент, так как он захештрован")