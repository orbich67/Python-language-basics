from functools import wraps


def type_logger(callback):
    @wraps(callback)
    def wrapper(*args):
        result_tmp = []
        for el in args:
            result_tmp.append(f'{callback.__name__}({el}: {type(el)})')
        result = '"'.join(result_tmp)
        return result.replace('"', ', ')

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    a = calc_cube(5, 5.0, [5], '5')
    print(a)
