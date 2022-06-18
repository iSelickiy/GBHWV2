# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово
# yield

def odd_nums(num):
    for res in range(1, num + 1, 2):
        yield res


odd_to_15 = odd_nums(15)
for i in odd_to_15:
    print(i)

# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя
# ключевое слово yield.
odd_to_15 = (i for i in range(1, 16, 2))
for i in odd_to_15:
    print(i)
