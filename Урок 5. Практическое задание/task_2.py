"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
hex()
"""

from collections import defaultdict


def list_converter(number):
    needed_list = []
    for i in number:
        needed_list.append(i)
    return needed_list


def sum_and_mul_hex():
    result = defaultdict(list)
    for c in range(1, 3):
        number = (input(f"Введите {c} число: "))
        list_converter(number)
        result[c] = list_converter(number)
    summary = hex(int(''.join(result[1]), 16) + int(''.join(result[2]), 16))
    result["sum"] = list_converter(summary[2:].upper())
    multiply = hex(int(''.join(result[1]), 16) * int(''.join(result[2]), 16))
    result["multiply"] = list_converter(multiply[2:].upper())
    return f"Сумма чисел: {result['sum']}", f"Произведение чисел: {result['multiply']}"


print(sum_and_mul_hex())
