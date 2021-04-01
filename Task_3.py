class Cell:
    def __init__(self, amount):
        self.amount = int(amount)

    def __str__(self):
        return f'{self.amount}'

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        if self.amount - other.amount > 0:
            return Cell(self.amount - other.amount)
        return f'Вычитание невозможно! Уменьшаемая клетка меньше по размеру.'

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __floordiv__(self, other):
        return Cell(self.amount // other.amount)

    def make_order(self, row):
        result = ''
        for i in range(self.amount // row):
            result += '*' * row + '\n'
        result += '*' * (self.amount % row)
        return result


if __name__ == '__main__':
    cell_1 = Cell(12)
    cell_2 = Cell(8)
    print('Сложение: ', cell_1 + cell_2, 'Вычитание: ', cell_1 - cell_2,
          'Умножение: ', cell_1 * cell_2, 'Деление: ', cell_1 // cell_2)
    print(cell_1.make_order(5))
    print(cell_2.make_order(3))
