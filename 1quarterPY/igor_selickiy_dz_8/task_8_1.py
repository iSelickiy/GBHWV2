# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения
# извлекает имя пользователя и почтовый домен из email адреса и возвращает их
# в виде словаря. Если адрес не валиден, выбросить исключение ValueError

import re


EMAIL = re.compile(r'([a-z0-9_\.]+)@([a-z0-9]+\.[a-z]+)')


def email_parse(email):
    found_info = EMAIL.findall(email)
    if found_info:
        name, addr = found_info[0]
    else:
        raise ValueError(f'wrong email: {email}')
    print(name, addr)


email_parse('i.selickiy@yandex.ru')
