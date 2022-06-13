# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self, type_stat=None):
        if type_stat is None:
            return f'Запускаю отрисовку неизвестным инструментом {self.title}'
        else:
            return f'Запускаю отрисовку {type_stat} {self.title}'


class Pen(Stationery):
    def draw(self, type_stat=None):
        return super(Pen, self).draw(type_stat='ручкой')


class Pencill(Stationery):
    def draw(self, type_stat=None):
        return super(Pencill, self).draw(type_stat='карандашом')


class Handle(Stationery):
    def draw(self, type_stat=None):
        return super(Handle, self).draw(type_stat='маркером')


pen = Pen('Eric Krauser')

print(pen.draw())
