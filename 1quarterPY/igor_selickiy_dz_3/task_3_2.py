# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
# возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
# "И": ["Иван", "Илья"],
# "М": ["Мария"],
# "П": ["Петр"]
# }

# (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
# и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего
# задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.

def thesaurus_adv(*args):
    contact_book = dict()
    for arg in args:
        surname_word = arg.split()[1][0]
        name_word = arg.split()[0][0]
        if surname_word in contact_book:
            if name_word in contact_book[surname_word]:
                contact_book[surname_word][name_word].append(arg)
            else:
                contact_book[surname_word].update({name_word: [arg]})
        else:
            contact_book.update({surname_word: {name_word: [arg]}})
    return contact_book


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

