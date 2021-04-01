from abc import ABC


class Clothes(ABC):
    def __init__(self):
        self._expense = 0

    def __str__(self):
        return f'Общий расход ткани на {self.__class__.__name__}: {self.expense:.2f}'

    @property
    def expense(self):
        if not self._expense:
            self._expense = self.consumption()
        return self._expense

    def consumption(self):
        raise NotImplementedError(self.__class__.__name__)

    def __add__(self, other):
        result = Clothes()
        result._expense = self.expense + other.expense
        return result


class Coat(Clothes):
    def __init__(self, param):
        super().__init__()
        self.param = param

    def __str__(self):
        return f'Расход ткани: {self.expense:.2f}'

    def consumption(self):
        return self.param / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, param):
        super().__init__()
        self.param = param

    def __str__(self):
        return f'Расход ткани: {self.expense:.2f}'

    def consumption(self):
        return 2 * self.param + 0.3


if __name__ == '__main__':
    coat_1 = Coat(52)
    coat_2 = Coat(50)
    costume_1 = Costume(185)
    costume_2 = Costume(175)
    print('coat_1.', coat_1)
    print('coat_2.', coat_2)
    print('costume_1.', costume_1)
    print('costume_2.', costume_2)
    print(coat_1 + coat_2 + costume_1 + costume_2)
