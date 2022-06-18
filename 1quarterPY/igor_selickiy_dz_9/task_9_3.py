# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

wage_and_bonus = {'wage': 100000, 'bonus': 5000}


class Worker:
    def __init__(self, name, surname, position):
        self._name = name
        self._surname = surname
        self._position = position
        self.__income = wage_and_bonus


class Position(Worker):
    def get_full_name(self):
        return f'{self._name} {self._surname}'

    def get_total_income(self):
        income = self._Worker__income
        return income['wage'] + income['bonus']


igor = Position(name='Igor', surname='Selickiy', position='Worker')
print(igor.get_full_name())
print(igor.get_total_income())
