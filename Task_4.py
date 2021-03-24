from functools import wraps


def val_checker(_func):
    def decor_val_checker(func):
        @wraps(func)
        def wrapper(num):
            if _func(num):
                return func(num)
            raise ValueError(f'wrong val {num}')

        return wrapper

    return decor_val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    a = calc_cube(5)
    print(a)
