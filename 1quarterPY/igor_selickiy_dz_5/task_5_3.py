# Есть два списка
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)
#
# Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в
# списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние
# кортежи в виде: (<tutor>, None)
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']


def zip_longest(arg1, arg2):
    counter = 0
    for i in arg1:
        if len(arg2) > counter:
            res = i, arg2[counter]
            counter += 1
            yield res
        else:
            yield i, None


# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.


zip_res = zip_longest(tutors, klasses)
print(type(zip_res))

for some in zip_res:
    print(some)
