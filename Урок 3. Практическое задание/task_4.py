"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


import hashlib
hash_dict = {}

def check_hash(url):
    salt = "80740ba2a1584aa7bf96d32bbe774e54"
    res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    r = hash_dict.get(res)
    if r is None:
        hash_dict[res] = url
        return "Ссылка добавлена в кэш"

check_hash("www.gooole.com")
check_hash("www.go22oole.com")
check_hash("www.gooole.com")
print(hash_dict)