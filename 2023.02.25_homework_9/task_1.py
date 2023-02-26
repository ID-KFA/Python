"""Создать не менее двух дескрипторов для атрибутов классов, которые вы
cоздали ранее в ДЗ"""


class NonNegative:
    """ Проверяет, чтобы пользователь не ввел отрицательное значение"""

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Thickness:
    """ Проверяет толщину асфальта. Должно быть не меньше 0.05 """

    def __set__(self, instance, value):
        if value < 0.05:
            raise ValueError("Введенное значение должно быть не меньше 0.05")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    """
    Автодорога
    """
    r_length = NonNegative()
    r_width = NonNegative()
    a_usage = NonNegative()
    a_thickness = Thickness()

    def asphalt_calc(self, r_length, r_width, a_usage, a_thickness):
        """
        :param r_length: Длина дороги в метрах
        :param r_width: Ширина дороги в метрах
        :param a_usage: Расход асфальта на один квадратный метр толщиной в 1 см
        :param a_thickness: Толщина асфальта
        :return: Масса асфальта в тоннах
        """
        self.r_length = r_length
        self.r_width = r_width
        self.a_usage = a_usage
        self.a_thickness = a_thickness

        return (
                self.r_length * self.r_width * self.a_usage *
                self.a_thickness) / 1000


road = Road()
print(
    f"Масса асфальта составит {round(road.asphalt_calc(5000, 20, 25, 0.04))} "
    f"тонн")
