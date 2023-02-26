"""Создать метакласс для паттерна Синглтон (см. конец вебинара)"""


class Singleton(type):
    """ Метакласс """
    a = None

    def __call__(cls, *args, **kwargs):
        if Singleton.a is None:
            Singleton.a = type.__call__(cls, *args, **kwargs)
        return Singleton.a


class MyClass(metaclass=Singleton):
    """ Класс на основе Метакласса """

    def method_1(self):
        """Тестовый метод"""


obj_1 = MyClass()
obj_2 = MyClass()
print(obj_1 is obj_2)
