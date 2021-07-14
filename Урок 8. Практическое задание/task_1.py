"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""


# Сделали упорядоченный список
def str_to_sorted_list(letters):
    return sorted([[letters.count(i), i] for i in set(letters)], key=lambda x: x[0])


# Сделали дерево хафмана
def haffman_tree(letters):
    new_list = str_to_sorted_list(letters)
    while len(new_list) > 1:
        new_value = new_list[0][0] + new_list[1][0]
        new_list_2 = [new_value, {0: new_list[0][1], 1: new_list[1][1]}]
        new_list.remove(new_list[1])
        new_list.remove(new_list[0])
        for i in range(len(new_list)):
            if new_value > new_list[i][0]:
                continue
            else:
                new_list.insert(i, new_list_2)
                break
        else:
            new_list.append(new_list_2)
    return new_list[0][1]


# Сделали кодировку символов
def haffman_code(tree, path='', code_table={}):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')
    return code_table


# Сделали перевод текста в кодовую таблицу
def letters_to_code(letters):
    code_letters = haffman_code(haffman_tree(letters))
    coded_letters = ""
    for i in letters:
        coded_letters += code_letters[i] + " "
    return coded_letters


words = "beep boop beer!"
# Выводим закодированную строку
print(letters_to_code(words))

