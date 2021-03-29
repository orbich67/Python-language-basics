class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина "{self.name}" поехала'

    def stop(self):
        return f'Машина "{self.name}" остановилась'

    def turn(self, direction):
        return f'Машина "{self.name}" повернула {direction}'

    def show_speed(self):
        return f'Текущая скорость автомобиля "{self.name}" составляет: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Скорость автомобиля {self.name} превышена и составляет: {self.speed}'
        return f'Текущая скорость автомобиля "{self.name}" составляет: {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Скорость автомобиля {self.name} превышена и составляет: {self.speed}'
        return f'Текущая скорость автомобиля "{self.name}" составляет: {self.speed}'


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    town = TownCar(65, 'Желтый', 'ПАЗ', is_police=False)
    print('1: ', vars(town))
    print(town.go(), town.stop(), town.turn('налево'), town.turn('направо'), town.show_speed(), sep='\n')

    sport = SportCar(120, 'Зеленый', 'Ауди', is_police=False)
    print('\n2: ', vars(sport))
    print(sport.go(), sport.stop(), sport.turn('налево'), sport.turn('направо'), sport.show_speed(), sep='\n')

    work = WorkCar(45, 'Красный', 'УАЗ', is_police=False)
    print('\n3: ', vars(work))
    print(work.go(), work.stop(), work.turn('налево'), work.turn('направо'), work.show_speed(), sep='\n')

    police = PoliceCar(60, 'Белый', 'ВАЗ', is_police=True)
    print('\n4: ', vars(police))
    print(police.go(), police.stop(), police.turn('налево'), police.turn('направо'), police.show_speed(), sep='\n')
