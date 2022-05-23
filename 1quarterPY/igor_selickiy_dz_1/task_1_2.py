# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень
# числа X):
# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
# делится нацело на 7. Внимание: использовать только арифметические операции!
# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
# списка, сумма цифр которых делится нацело на 7.
# c. * Решить задачу под пунктом b, не создавая новый список.

cube_list = []
res = 0
res_17 = 0
res_17_additional = 0

for item in range(1, 1000, 2):
    cube_list.append(item ** 3)
    
for item in cube_list:
    summ = 0
    num_1 = item
    num_17 = item + 17
    num_17_add = int(str(item) + '17')
    while num_1 > 0:
        summ += num_1 % 10
        num_1 = num_1 // 10
    if not summ % 7: 
        res += item
# 1+17 = 18
    summ = 0
    while num_17 > 0:
        summ += num_17 % 10
        num_17 = num_17 // 10
    if not summ % 7:
        res_17 += item + 17
# 1+17 = 117
    summ = 0
    while num_17_add > 0:
        summ += num_17_add % 10
        num_17_add = num_17_add // 10
    if not summ % 7: 
        res_17_additional += int(str(item) + '17')
    summ = 0


print(res)
print(res_17)
print(res_17_additional)

