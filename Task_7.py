class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b < 0:
            return f'({self.a}{self.b}j)'
        return f'({self.a}+{self.b}j)'

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b)


if __name__ == '__main__':
    c_1 = ComplexNumber(3, 1)
    c_2 = ComplexNumber(2, -3)
    print(c_1 + c_2, c_1 * c_2)

    # Проверка результата используя класс complex()
    a_1 = complex(3, 1)
    a_2 = complex(2, -3)
    print(a_1 + a_2, a_1 * a_2)
