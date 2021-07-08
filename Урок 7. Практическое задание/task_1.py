"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_1(lst_obj):
    n = 1
    while n < len(lst_obj):
        k = 0
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                k += 1
        if k < 1:
            break
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(orig_list[:])
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(bubble_sort(orig_list[:]))

print(orig_list[:])
print(
    timeit.timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))
print(bubble_sort(orig_list[:]))

orig_list = [random.randint(-100, 100) for _ in range(100)]
print(orig_list[:])
# замеры 100
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(bubble_sort(orig_list[:]))

print(orig_list[:])
# замеры 100
print(
    timeit.timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))
print(bubble_sort(orig_list[:]))

orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(orig_list[:])
# замеры 1000
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(bubble_sort(orig_list[:]))

print(orig_list[:])
# замеры 1000
print(
    timeit.timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))
print(bubble_sort(orig_list[:]))
"""
Замеры без проверки на отсортированность списка (bubble_sort)
0.011858499999999994 на 10
0.7551486999999999 на 100
80.8147877 на 1000

Замеры c проверкой на отсортированность списка (bubble_sort_1)
0.011229199999999995 на 10
0.7415603 на 100
87.03331890000001 на 1000
Вывод: проверка не нужна, она даже увеличивает время при сортировке более длинного списка
"""