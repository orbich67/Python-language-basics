class CustomError(Exception):
    pass


def division(divisible, divisor):
    if divisor == 0:
        raise CustomError(f'Делить на ноль нельзя!')
    return divisible / divisor


def main():
    try:
        divisible = float(input('Введите делимое: '))
        divisor = float(input('Введите делитель: '))
        print(division(divisible, divisor))
    except CustomError as e:
        print(e)


if __name__ == '__main__':
    main()
