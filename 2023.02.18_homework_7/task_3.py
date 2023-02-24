"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage,
"bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать публичные методы получения полного имени сотрудника (get_full_name)
 и дохода с учетом премии
(get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку
str
str(self) - вызывается функциями str, print и format. Возвращает строковое
представление объекта.
"""


class Worker:
    """ Содержит Имя, Фамилию, должность и доход работника """
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position

        self.income = _income


class Position(Worker):
    """ Описывает должность работника """
    def get_full_name(self):
        """ Получает имя работника """

        return f"{self.name} {self.surname}"

    def get_total_income(self):
        """ Получает доход работника """
        return f"{self.income['wage'] + self.income['bonus']}"

    def __str__(self):
        return f"Работник: {self.name} {self.surname}, " \
               f"Должность: {self.position}, Оклад: {self.income['wage']} " \
               f"рублей, Премия: {self.income['bonus']} рублей."


worker_1 = Position("Антон", "Новоселов", "Разработчик",
                    {"wage": 1200, "bonus": 2200})
worker_2 = Position("Вероника", "Новоселова", "Тестер",
                    {"wage": 2000, "bonus": 3200})

# print(worker_1.name)
# print(worker_1.position)
# print(worker_1.income)
# print(worker_2.income)

print(f"Работник: {worker_1.get_full_name()}, доход: "
      f"{worker_1.get_total_income()} рублей.")
print(f"Работник: {worker_2.get_full_name()}, доход: "
      f"{worker_2.get_total_income()} рублей.")
print()

print(worker_1)
print(worker_2)
