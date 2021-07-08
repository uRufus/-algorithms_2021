"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import timeit
import random


def merge_sort(x):
    if len(x) < 2:
        return x
    result = []
    mid = int(len(x) / 2)
    left = merge_sort(x[:mid])
    right = merge_sort(x[mid:])
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result += left[i:]
    result += right[j:]
    return result


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(f"Исходный: {orig_list[:]}")
# замеры 10
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(f"Отсортированный: {merge_sort(orig_list[:])}")

orig_list = [random.randint(-100, 100) for _ in range(100)]
print(f"Исходный: {orig_list[:]}")
# замеры 100
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(f"Отсортированный: {merge_sort(orig_list[:])}")

orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(f"Исходный: {orig_list[:]}")
# замеры 1000
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(f"Отсортированный: {merge_sort(orig_list[:])}")

"""
0.018803400000000005 на 10
0.27611389999999997 на 100
3.4875171000000003 на 1000
"""