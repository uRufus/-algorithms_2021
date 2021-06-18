"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

# Вариант решения

class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        if len(self.elems) == 0:
            self.elems.append([])
        if len(self.elems[-1]) < 5:
            self.elems[-1].append(el)
        else:
            self.elems.append([])
            self.elems[-1].append(el)

    def pop_out(self):
        if len(self.elems) == 0:
            return self.elems == []
        if len(self.elems[-1]) > 1:
            return self.elems[-1].pop()
        else:
            pop_el = self.elems[-1].pop()
            self.elems.pop()
            print(self.elems)
            return pop_el

    def get_val(self):
        if len(self.elems) == 0:
            return "Нет тарелок"
        return self.elems[-1][-1]

    def stack_size(self):
        if len(self.elems) > 1:
            return 5 * (len(self.elems) - 1) + len(self.elems[-1])
        return len(self.elems[-1])


if __name__ == '__main__':

    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стопки
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(10)

    SC_OBJ.push_in('code')

    # Удаляем елементы из стопок
    SC_OBJ.pop_out()
    SC_OBJ.pop_out()
    print(SC_OBJ.elems)

    # Повторно наполняем стопки
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(10)

    # получаем значение первого элемента с вершины стопки, но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())

    # узнаем размер стопок
    print(SC_OBJ.stack_size())


