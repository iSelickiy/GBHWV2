# Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на
# экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

for percent in range(101):
    if percent in range(10, 20):
        name = 'процентов'
    elif str(percent)[-1] == '1':
        name = 'процент'
    elif str(percent)[-1] == '2' or str(percent)[-1] == '3' or str(percent)[-1] == '4':
        name = 'процента'
    else:
        name = 'процентов'

    print(f'{percent} {name}')
