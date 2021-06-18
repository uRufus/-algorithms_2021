"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

# Вариант решения

class StackClass:
    def __init__(self):
        self.base = []
        self.in_progress = []
        self.completed = []
        self.reworked = []
        self.tasks = ["base", "in_progress", "completed", "reworked"]

    def is_empty(self):
        return self.base == [], self.in_progress == [], self.completed == [], self.reworked == []

    def push_in_new_task(self, el):
        self.base.append(el)

    def move_task_to(self, a, b, c):
        d = self.tasks.index(a)
        e = self.tasks.index(b)
        if d == 0:
            if c in self.base:
                self.base.remove(c)
            else:
                return "Нет такой задачи"
        elif d == 1:
            if c in self.in_progress:
                self.in_progress.remove(c)
            else:
                return "Нет такой задачи"
        elif d == 2:
            if c in self.completed:
                self.completed.remove(c)
            else:
                return "Нет такой задачи"
        elif d == 3:
            if c in self.reworked:
                self.reworked.remove(c)
            else:
                return "Нет такой задачи"
        else:
            return "Задача не найдена"
        if e == 0:
            self.base.append(c)
        elif e == 1:
            self.in_progress.append(c)
        elif e == 2:
            self.completed.append(c)
        elif e == 3:
            self.reworked.append(c)
        else:
            return "Нет такого статуса задач"




if __name__ == '__main__':

    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стопки
    SC_OBJ.push_in_new_task(10)
    SC_OBJ.push_in_new_task('code')
    SC_OBJ.push_in_new_task(False)
    SC_OBJ.push_in_new_task(5.5)
    SC_OBJ.push_in_new_task(10)

    SC_OBJ.push_in_new_task('code')

    # Удаляем елементы из стопок
    print(SC_OBJ.in_progress)
    SC_OBJ.move_task_to("base", "in_progress", 10)
    print(SC_OBJ.in_progress)
    SC_OBJ.move_task_to("in_progress", "completed", 10)
    print(SC_OBJ.in_progress)
    print(SC_OBJ.base)
    print(SC_OBJ.completed)
