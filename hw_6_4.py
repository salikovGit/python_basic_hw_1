class Car:
    def __init__(self, speed: int, color, name, is_police: bool = False):
        self.speed: int = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} в движении')

    def stop(self):
        print(f'{self.name} стоит')

    def turn_right(self):
        print(f'{self.name} повернул(а) направо')

    def turn_left(self):
        print(f'{self.name} повернула(а) налево')

    def show_speed(self):
        print(f'Скорость {self.name} составляет {self.speed: int} км\ч')


class TownCar(Car):

    def __init__(self, speed: int, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} составляет {self.speed: int} км\ч')
        if self.speed > 40:
            print(f'Скорость {self.name} больше допустимой')


class SportCar(Car):
    def __init__(self, speed: int, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed: int, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} составляет {self.speed: int} км\ч')

        if self.speed > 60:
            print(f'Скорость {self.name} больше допустимой')


class PoliceCar(Car):
    def __init__(self, speed: int, color, name, is_police):
        super().__init__(speed, color, name, is_police)


BMW = SportCar(140, 'Black', 'BMW', False)
Bentley = TownCar(70, 'Blue', 'Bentley', False)
vaz_14 = WorkCar(70, 'White', 'Vaz 21014', True)
Nissan = TownCar(110, 'Blue', 'Nissan', False)
vaz_14.turn_left()
Bentley.turn_right()
BMW.stop()
Nissan.show_speed
print(Nissan.is_police)
