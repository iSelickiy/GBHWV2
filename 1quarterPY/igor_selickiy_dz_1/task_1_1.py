# Реализовать вывод информации о промежутке времени в зависимости от его
# продолжительности duration в секундах:
# a. до минуты: <s> сек;
# b. до часа: <m> мин <s> сек;
# c. до суток: <h> час <m> мин <s> сек;
# d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.


duration = 86400+3600+60+1

time_duration = {86400: 'дн', 3600: 'час', 60: 'мин', 1: 'сек'}
res = []


for time, name in time_duration.items():
    num = duration // time
    if num > 0:
        res.append(f'{num} {name}')
        duration = duration % time


print(' '.join(res))
