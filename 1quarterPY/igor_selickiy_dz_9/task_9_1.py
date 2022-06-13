# Создать класс TrafficLight (светофор):
# ● определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт.
import time


class TrafficLight:

    def __init__(self):
        self._color = {'Red': 7, 'Yellow': 2, 'Green': 10}

    def change_color(self):
        for light_color, light_time in self._color.items():
            print(light_color)
            time.sleep(light_time)

        #Вечный светофор
        # while True:
        #     self._color = 'red'
        #     print(self._color)
        #     time.sleep(7)
        #     self._color = 'Yellow'
        #     print(self._color)
        #     time.sleep(2)
        #     self._color = 'Green'
        #     print(self._color)
        #     time.sleep(10)


traffic1 = TrafficLight()
traffic1.change_color()
