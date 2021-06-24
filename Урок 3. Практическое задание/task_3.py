"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

def unique_func(a):
    new_list = []
    string = hash(a)
    while len(a) > 0:
        for i in range(len(a)):
            for b in range(len(a[i:])):
                if string != hash(a[i:b + 1]) != hash("")and hash(a[i:b + 1]) not in new_list:
                    new_list.append(hash(a[i:b + 1]))
        a = a[1:]
    return len(new_list)
print(unique_func("papa"))



