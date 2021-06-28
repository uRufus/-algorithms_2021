"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000

Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма.

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснование результатам.
"""
import timeit

# O(n ** 2)
def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))


# O(n log n)
def complex(k):
    n = k * 10
    x = [i for i in range(2, n + 1)]
    for i in x:
        c = i * i
        while c <= n * 10:
            if c in x:
                x.remove(c)
            c += i

    return x[k - 1]
k = int(input('Введите порядковый номер искомого простого числа: '))
print(complex(k))

print("Сравнение скорости алгоритмов при искомом числе 10. Без решета")
print(timeit.timeit("simple(10)", globals=globals(), number=10))
print("Сравнение скорости алгоритмов при искомом числе 10. Через решето")
print(timeit.timeit("complex(10)", globals=globals(), number=10))

print("Сравнение скорости алгоритмов при искомом числе 100. Без решета")
print(timeit.timeit("simple(100)", globals=globals(), number=10))
print("Сравнение скорости алгоритмов при искомом числе 100. Через решето")
print(timeit.timeit("complex(100)", globals=globals(), number=10))

print("Сравнение скорости алгоритмов при искомом числе 1000. Без решета")
print(timeit.timeit("simple(1000)", globals=globals(), number=10))
print("Сравнение скорости алгоритмов при искомом числе 1000. Через решето")
print(timeit.timeit("complex(1000)", globals=globals(), number=10))

'''
Функция решета эратосфена работает медленнее за счет большей сложности алгоритма, особенно это видно на большом 
значении искомого числа
'''