"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""
import timeit
from collections import deque
# Создание списка и очереди
test_deque = deque([2, 1, 3, 4, 5])
test_list = [2, 1, 3, 4, 5]

print("Замер скорости при создании deque с элементами")
print(timeit.timeit("test_deque = deque([2, 1, 3, 4, 5])", globals=globals()))
print("Замер скорости при создании list с элементами")
print(timeit.timeit("test_list = [2, 1, 3, 4, 5]", globals=globals()))

print("Замер скорости при добавлении элемента в конец deque")
print(timeit.timeit("test_deque.append(7)", globals=globals()))
print("Замер скорости при добавлении элемента в конец list")
print(timeit.timeit("test_list.append(7)", globals=globals()))

print("Замер скорости при удалении последнего элемента в deque")
print(timeit.timeit("test_deque.pop()", globals=globals()))
print("Замер скорости при удалении последнего элемента в list")
print(timeit.timeit("test_list.pop()", globals=globals()))

print("Замер скорости при добавлении элемента в начало deque")
print(timeit.timeit("test_deque.appendleft(23)", globals=globals(), number=10000))
print("Замер скорости при добавлении элемента в начало list")
print(timeit.timeit("test_list.insert(0, 23)", globals=globals(), number=10000))

print("Замер скорости при удалении первого элемента в deque")
print(timeit.timeit("test_deque.popleft()", globals=globals(), number=10000))
print("Замер скорости при удалении первого элемента в list")
print(timeit.timeit("test_list.pop(0)", globals=globals(), number=10000))

'''
deque выигрывает немного list по скорости при создании списка, добавлении элемента в конец списка,
удалении элемента из конца списка.
deque сильно выигрывает list в скорости при использовании встроенных функций 
по добавлению и удалению элемента из начала списка.
Вывод: deque работает быстрее list.
'''
