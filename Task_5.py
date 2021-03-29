class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки красками.'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки ручкой.'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки карандашем.'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки маркером.'


if __name__ == '__main__':
    stat_1 = Stationery('краски')
    pen_1 = Pen('ручка')
    pencil_1 = Pencil('карандаш')
    handle_1 = Handle('маркер')
    print(stat_1.draw(), pen_1.draw(), pencil_1.draw(), handle_1.draw(), sep='\n')
