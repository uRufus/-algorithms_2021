"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""
import timeit
# O(n)
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
# O(1)
def func_2(nums):
    return [i for i, v in enumerate(nums) if v % 2 == 0]

l = [i for i in range(10)]
print(timeit.timeit("func_1(l)", globals=globals()))
print(timeit.timeit("func_2(l)", globals=globals()))

# func_2 выполняется быстрее из-за константной сложности в то время когда у func_1 линейная сложность