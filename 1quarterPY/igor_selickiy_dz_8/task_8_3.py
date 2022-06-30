# 3. Написать декоратор для логирования типов позиционных аргументов функции


from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)

    return wrapper


@type_logger
def calc_cube(*args):
    return list(map(lambda x: x ** 3, args))


some = calc_cube(7, 8)


print(some)
print(f'{calc_cube.__name__}, {calc_cube.__doc__}')
