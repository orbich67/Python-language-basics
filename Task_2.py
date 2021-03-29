class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_asphalt_mass(self, weight, layer):
        result = self._length * self._width * weight * layer / 1000
        return f'{self._length}м * {self._width}м * {weight}кг * {layer}см = {int(result)} т.'


if __name__ == '__main__':
    way_1 = Road(20, 5000)
    print(way_1.calc_asphalt_mass(25, 5))
