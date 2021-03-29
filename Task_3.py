class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"Оклад": float(wage), "Премия": float(bonus)}


class Position(Worker):

    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income["Оклад"] + self._income["Премия"]


if __name__ == '__main__':
    employee_1 = Position('Александр', 'Петров', 'кладовщик', 15000, 3000)
    employee_2 = Position('Никита', 'Павлов', 'водитель', 20000, 2000)
    print('Значения атрибутов: ', vars(employee_1))
    print('Значения атрибутов: ', vars(employee_2))
    print(employee_1.get_full_name(), employee_1.get_total_income())
    print(employee_2.get_full_name(), employee_2.get_total_income())
