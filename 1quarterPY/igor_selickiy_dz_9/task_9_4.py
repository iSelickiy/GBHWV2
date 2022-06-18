# 4. Реализуйте базовый класс Car:
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_polise=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_polise

    def go(self):
        return f'Now car ride'

    def stop(self):
        return f'Car stopping'

    def turn(self, direction):
        return f'Car turn {direction}'

    def show_speed(self, stop_remind=False):
        if stop_remind is True:
            return f'{self.speed} km/h, slow down the speed!'
        else:
            return f'{self.speed} km/h'


class TownCar(Car):
    def show_speed(self, stop_remind=False):
        __max_speed = 60
        return super().show_speed(stop_remind=True) if int(self.speed) > __max_speed else super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self, stop_remind=False):
        __max_speed = 40
        return super().show_speed(stop_remind=True) if int(self.speed) > __max_speed else super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_polise=True):
        super().__init__(speed, color, name, is_polise)


pol_car = PoliceCar(speed=100, color='Blue', name='Ford Focus')
print(pol_car.is_police)
print(pol_car.show_speed())

town_car = TownCar(speed=100, color='Blue', name='Ford Focus')
print(town_car.is_police)
print(town_car.show_speed())
print(town_car.turn('left'))
