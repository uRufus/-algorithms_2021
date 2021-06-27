"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
import timeit
array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

def func_3():
    most_common = None
    max_counts = 0
    for item in set(array):
        qty = array.count(item)
        if qty > max_counts:
            max_counts = qty
            most_common = item
    return f'Чаще всего встречается число {most_common}, ' \
           f'оно появилось в массиве {max_counts} раз(а)'

print(func_1())
print(func_2())
print(func_3())

print(timeit.timeit("func_1()", globals=globals(), number=1000000))
print(timeit.timeit("func_2()", globals=globals(), number=1000000))
print(timeit.timeit("func_3()", globals=globals(), number=1000000))
'''
Получилось ускорить задачу, так как func_3 имеет константную сложность 
в то время как остальные имеют линейную сложность.
'''
