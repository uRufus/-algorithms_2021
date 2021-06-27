"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
import timeit
from cProfile import run

#О(log n)
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)

# O(n)
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

# O(1)
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

#O(n)
def revers_4(enter_num):
    p = ""
    for i in str(enter_num):
            p = i + p
    return p




def num(n):
    l = ""
    for i in range(1, n):
            l += str(i)
    l = int(l)
    return l
l = num(360)
k = num(20)
run('revers_1(l)')
print(timeit.timeit("revers_1(k)", globals=globals()))
run('revers_2(l)')
print(timeit.timeit("revers_2(k)", globals=globals()))
run('revers_3(l)')
print(timeit.timeit("revers_3(k)", globals=globals()))
run('revers_4(l)')
print(timeit.timeit("revers_4(k)", globals=globals()))

'''
Самая быстрая revers_3 так как у нее константная сложность.
reverse_1 самая медленная так как у нее логарифмическая сложность
У reverse_2 и reverse_4 одинаковая линейная сложность, однако  reverse 4 имеет меньше строчек кода и 
выигрывает в скорости при большом числе
'''
