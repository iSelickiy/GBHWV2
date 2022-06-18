# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;

class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate(self, weight, thickness):
        return self.__width * self.__length * weight * thickness


some_road = Road(length=10, width=15)
print(some_road.calculate(weight=10, thickness=10))
