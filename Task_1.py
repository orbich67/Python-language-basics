class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        mat_st = ''
        for row in self.matrix_list:
            for i in row:
                mat_st += f'{i:4}'
            mat_st += '\n'
        return mat_st

    def __add__(self, other):
        for i in range(len(self.matrix_list)):
            for j in range(len(other.matrix_list[i])):
                self.matrix_list[i][j] = self.matrix_list[i][j] + other.matrix_list[i][j]
        return Matrix(self.matrix_list)


if __name__ == '__main__':
    mat_1 = Matrix([[6, 6, 25], [12, 0, 3], [-11, 21, -18]])
    mat_2 = Matrix([[-3, -1, 7], [-10, 4, 3], [10, 43, 10]])
    print(f'mat_1:\n{mat_1}')
    print(f'mat_2:\n{mat_2}')
    print(f'Sum:\n{mat_1 + mat_2}')
