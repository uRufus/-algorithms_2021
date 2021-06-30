"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""
from collections import namedtuple


def firms_ave_profit():
    number_of_firms = int(input("Введите количество фирм: "))
    firms = namedtuple('Firms', 'firm first second third fourth ave')
    list_of_firms = []
    for i in range(number_of_firms):
        firm_name = input("Введите название фирмы: ")
        profit = (input("Введите прибыль фирмы: ")).split()
        i = firms(
            firm=firm_name,
            first=int(profit[0]),
            second=int(profit[1]),
            third=int(profit[2]),
            fourth=int(profit[3]),
            ave=((int(profit[0]) + int(profit[1]) + int(profit[2]) + int(profit[3])) / 4)
        )
        list_of_firms.append(i)
    average_profit = 0
    for i in range(len(list_of_firms)):
        average_profit += list_of_firms[0].ave
    average_profit /= len(list_of_firms)
    print(f"Средняя годовая прибыль всех предприятий: {average_profit}")
    firms_above_ave = []
    firms_below_ave = []
    for i in range(len(list_of_firms)):
        firms_above_ave.append(list_of_firms[i].firm) \
            if list_of_firms[i].ave >= average_profit else firms_below_ave.append(list_of_firms[i].firm)
    print(f"Предприятия, с прибылью выше среднего значения: {firms_above_ave}")
    print(f"Предприятия, с прибылью ниже среднего значения: {firms_below_ave}")


firms_ave_profit()

