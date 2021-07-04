"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
import random
import timeit
from memory_profiler import memory_usage
from numpy import array


# Создаем декоратор для замера скорости и времени
def check_time(func):
    def decor(*args, **kwargs):
        start_val = timeit.default_timer()
        mem1 = memory_usage()
        return_value = func(*args, **kwargs)
        end_val = timeit.default_timer()
        mem2 = memory_usage()
        print(f'Операция заняла {end_val - start_val} сек')
        print(f'Операция заняла {mem2[0] - mem1[0]} Mib')
        return return_value

    return decor


# 1 Скрипт
'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''
# Изначальное решение
first_list = [random.randint(1, 100) for i in range(0, 1000000)]
# new_list = [first_list[i] for i in range(1, len(first_list)) if first_list[i] > first_list[i - 1]]
# print(new_list)


# Преобразуем решение в функцию для замера памяти
@check_time
def new_list(numbers):
    return [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]


new_list(first_list)


# Новое решение
@check_time
def new_list_2(numbers):
    return array([numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]])


new_list_2(first_list)

'''
Вывод по 1 скрипту
Замеры изначального варианта
Операция заняла 0.2446408 сек
Операция заняла 3.82421875 Mib
Замеры после преобразования
Операция заняла 0.2919274999999999 сек
Операция заняла 1.88671875 Mib

Для нового решения мы использовали функцию array модуля numpy. Как видно из замеров, функция array позволила
уменьшить потребление памяти в 2 раза при небольшом увеличении в скорости.
'''

# 2 Скрипт

'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе
определить параметры, общие для приведенных типов. В классах-наследниках реализовать
параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы,
отвечающие за приём оргтехники на склад и передачу в определенное
подразделение компании. Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
вводимых пользователем данных. Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''


# Изначальное решение
class Warehouse:
    stocks = {}

    def move_to_stock(self, title: str, qty: int):
        if title in self.stocks:
            self.stocks[title]["stock"] += qty
        else:
            self.stocks.update({title: {"stock": qty}})
        return self.stocks

    def move_to_office(self, title: str, qty: int, office_dep: str):
        if title in self.stocks:
            if self.stocks[title]["stock"] >= qty:
                if "office" in self.stocks[title]:
                    if office_dep in self.stocks[title]["office"]:
                        self.stocks[title]["office"][office_dep] += qty
                    else:
                        self.stocks[title]["office"][office_dep] = qty
                else:
                    self.stocks[title].update({"office": {office_dep: qty}})
                self.stocks[title]["stock"] -= qty
                return self.stocks
            else:
                print(f"Не хватает количества товара {title} на складе. "
                      f"Остаток на складе: {self.stocks[title]['stock']}")
        else:
            print(f"Нет товара {title} на складе")


class OfficeEquipment:
    def __init__(self, title: str, height: int, length: int, width: int, weight: int):
        self.title = title
        self.height = height
        self.length = length
        self.width = width
        self.weight = weight


class Printer(OfficeEquipment):
    ink_volume = 100


class Scanner(OfficeEquipment):
    scans_per_min = 5


class Xerox(OfficeEquipment):
    copies_per_min = 10


@check_time
def first_run():
    printer = Printer("printer", 30, 40, 50, 60)
    scanner = Scanner("scanner", 40, 50, 60, 70)
    warehouse1 = Warehouse()
    warehouse1.move_to_stock(printer.title, 2)
    warehouse1.move_to_stock(scanner.title, 3)
    print(warehouse1.stocks)
    warehouse1.move_to_office(printer.title, 1, "IT department")
    print(warehouse1.stocks)
    warehouse1.move_to_office(printer.title, 1, "IT department")
    print(warehouse1.stocks)
    warehouse1.move_to_office(printer.title, 1, "IT department")
    print(warehouse1.stocks)


first_run()


# Новое решение
class Warehouse2:
    __slots__ = ['stocks']

    def __init__(self):
        self.stocks = {}

    def move_to_stock(self, title: str, qty: int):
        if title in self.stocks:
            self.stocks[title]["stock"] += qty
        else:
            self.stocks.update({title: {"stock": qty}})
        return self.stocks

    def move_to_office(self, title: str, qty: int, office_dep: str):
        if title in self.stocks:
            if self.stocks[title]["stock"] >= qty:
                if "office" in self.stocks[title]:
                    if office_dep in self.stocks[title]["office"]:
                        self.stocks[title]["office"][office_dep] += qty
                    else:
                        self.stocks[title]["office"][office_dep] = qty
                else:
                    self.stocks[title].update({"office": {office_dep: qty}})
                self.stocks[title]["stock"] -= qty
                return self.stocks
            else:
                print(f"Не хватает количества товара {title} на складе. "
                      f"Остаток на складе: {self.stocks[title]['stock']}")
        else:
            print(f"Нет товара {title} на складе")


class OfficeEquipment2:
    __slots__ = ['title', 'height', 'length', 'width', 'weight']

    def __init__(self, title: str, height: int, length: int, width: int, weight: int):
        self.title = title
        self.height = height
        self.length = length
        self.width = width
        self.weight = weight


class Printer(OfficeEquipment2):
    ink_volume = 100


class Scanner(OfficeEquipment2):
    scans_per_min = 5


class Xerox(OfficeEquipment2):
    copies_per_min = 10


@check_time
def second_run():
    printer2 = Printer("printer", 30, 40, 50, 60)
    scanner2 = Scanner("scanner", 40, 50, 60, 70)
    warehouse2 = Warehouse2()
    warehouse2.move_to_stock(printer2.title, 2)
    warehouse2.move_to_stock(scanner2.title, 3)
    print(warehouse2.stocks)
    warehouse2.move_to_office(printer2.title, 1, "IT department")
    print(warehouse2.stocks)
    warehouse2.move_to_office(printer2.title, 1, "IT department")
    print(warehouse2.stocks)
    warehouse2.move_to_office(printer2.title, 1, "IT department")
    print(warehouse2.stocks)


second_run()

'''
Вывод по 2 скрипту
Замеры изначального варианта
Операция заняла 0.09403449999999991 сек
Операция заняла 0.00390625 Mib
Замеры после преобразования
Операция заняла 0.09997659999999997 сек
Операция заняла 0.0 Mib

Для нового решения мы использовали __slots__ для хранения атрибутов класса в виде списка. 
Как видно из замеров, __slots__ позволила уменьшить потребление памяти.
'''


# 3 Скрипт

# Начальное значение
@check_time
def func_1(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


# Новое решение
def func_2(nums):
    for i in range(len(nums)):
        if int(nums[i]) % 2 == 0:
            yield nums


@check_time
def func_2_test(nums):
    return [i for i in func_2(nums)]


list_script_3 = [i for i in range(1000000)]
func_1(list_script_3)
func_2_test(list_script_3)
'''
Вывод по 3 скрипту
Замеры изначального варианта
Операция заняла 0.3046913 сек
Операция заняла 19.37890625 Mib
Замеры после преобразования
Операция заняла 0.4008469000000001 сек
Операция заняла 3.8125 Mib

Для нового решения мы использовали yield для того, чтобы не хранить список в памяти, а выбирать по элементу. 
Как видно из замеров, yield позволила уменьшить потребление памяти почти в 5 раз.
'''
