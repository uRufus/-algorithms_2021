"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

users = {
    "ABC": [10000, True],
    "BCD": [10000, True],
    "CDE": [10000, False],
    "DEF": [10000, False],
    "ZZZ": [10000, True]
             }

# 1 Вариант
# Сложность: O(n) - линейная.
def check_account(login, password):
    if login in users.keys():
        if users[login][0] == password:
            if users[login][1] == 1:
                return "Добро пожаловать на ресурс"
            else:
                return "Ваша учетная запись деактивирована"
        else:
            return "Неправильный пароль"
    else:
        answer = input("Хотите пройти аутентификацию в системе?(д)а или (н)ет?")
        if answer == "д":
            users[login] = [password, True]
        return "Добро пожаловать на ресурс"


print(check_account("CDE", 10000))
print(check_account("ZBD", 10000))
print(users)

# 2 Вариант
# Сложность: O(n log n) - Линейно-логарифмическая
def check_account_second_version(login, password):
    for k in sorted(users, key=users.get, reverse=True):
        if k == login:
            if users[login][0] == password:
                if users[login][1] == 1:
                    return "Добро пожаловать на ресурс"
                else:
                    return "Ваша учетная запись деактивирована"
            else:
                return "Неправильный пароль"
    answer = input("Хотите пройти аутентификацию в системе?(д)а или (н)ет?")
    if answer == "д":
        users[login] = [password, True]
        return "Добро пожаловать на ресурс"


print(check_account_second_version("CDE", 10000))
print(check_account_second_version("ZBD", 10000))
print(users)

# 3 Вариант
# Сложность: O(1) - константная
def check_account_third_version(login, password):
    if users.get(login):
        if users[login][0] == password:
            if users[login][1] == 1:
                return "Добро пожаловать на ресурс"
            else:
                return "Ваша учетная запись деактивирована"
        else:
            return "Неправильный пароль"
    answer = input("Хотите пройти аутентификацию в системе?(д)а или (н)ет?")
    if answer == "д":
        users[login] = [password, True]
        return "Добро пожаловать на ресурс"


print(check_account_third_version("CDE", 10000))
print(check_account_third_version("ZBD", 10000))
print(users)
# Первое решение лучше, так как линейная функция менее затратна чем линейно-логарифмическая
