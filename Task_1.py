from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = ['красный', 'желтый', 'зеленый']

    def running(self):
        state = 0
        while True:
            if state == 0:
                print(self.__color[state])
                sleep(7)
                state += 1
            elif state == 1:
                print(self.__color[state])
                sleep(2)
                state += 1
            elif state == 2:
                print(self.__color[state])
                sleep(3)
                state += 1
            else:
                state = 0


if __name__ == '__main__':
    run = TrafficLight()
    run.running()
