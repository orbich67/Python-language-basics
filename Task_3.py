class CustomError(Exception):
    pass


class CheckElements:
    def __init__(self):
        self.numbers = []

    @staticmethod
    def is_number(number):
        try:
            float(number)
            return True
        except ValueError:
            raise CustomError

    def check_value(self):
        while True:
            user_value = input('Input the numbers. Input "stop" to exit: ').lower()
            for el in user_value.split(' '):
                try:
                    if CheckElements.is_number(el):
                        self.numbers.append(el)
                except CustomError:
                    if el == 'stop':
                        return self.numbers
                    print(f'{el} not a number!')


if __name__ == '__main__':
    run = CheckElements()
    print(run.check_value())
