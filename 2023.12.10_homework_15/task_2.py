"""
Возьмите любые 1-3 задания из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей
параметров. Данная промежуточная аттестация оценивается по системе
"зачет" / "не зачет" "Зачет" ставится, если Слушатель успешно выполнил задание.
"Незачет" ставится, если Слушатель не выполнил задание. Критерии оценивания:
1 - Слушатель написал корректный код для задачи, добавил к ним логирование
ошибок и полезной информации.
"""
import logging
import argparse

logging.basicConfig(filename='Log/log_1.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке '
                           '{lineno} функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def decor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(
            f'функция: {func.__name__}, аргументы функции: {args},'
            f' результат функции: {result} ')
        return result

    return wrapper


class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str,
                 age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    @decor
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def birthday(self):
        self._age += 1
        if self._age == 61:
            raise WrongAgeError(self._age)

    @decor
    def get_age(self):
        return self._age


class Employee(Person):

    def __init__(self, last_name: str, first_name: str, patronymic: str,
                 age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        if 18 <= self._age <= 60:
            self.position = position.title()
            self.salary = salary
            logger.info(
                f'Принят новый работник: {self.last_name} {self.first_name} '
                f'{self.patronymic}, {self._age} лет, должность: '
                f'{self.position}, '
                f'зарплата: {self.salary} рублей')
        else:
            raise WrongAgeError(self._age)

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)
        logger.info(f'Работнику {self.last_name} {self.first_name} '
                    f'{self.patronymic} увеличили зарплату на '
                    f'{percent} процентов. '
                    f'Теперь она равна: {self.salary}')

    @decor
    def get_salary(self):
        logger.info(
            f'зарплата равна: {self.salary}')
        return self.salary

    def __str__(self):
        return f'{self.full_name()} ({self.position})'


class UserException(Exception):
    pass


class WrongAgeError(UserException):
    def __init__(self, value):
        self.value = value
        logger.error("Возраст работника должен находиться в пределах от 18 "
                     "до 60 лет.")

    def __str__(self):
        return f"Возраст работника должен находиться в пределах от 18 до " \
               f"60 лет. " \
               f"Вы ввели {self.value}"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Создаем нового работника")
    parser.add_argument('-ln', type=str, default='Иванов')
    parser.add_argument('-n', type=str, default='Иван')
    parser.add_argument('-p', type=str, default='Иванович')
    parser.add_argument('-age', type=int, default=20)
    parser.add_argument('-pos', type=str, default="Техник")
    parser.add_argument('-sal', type=float, default=10000)

    # p1 = Person("Сергеев", "Яков", "Михайлович", 50)
    # e1 = Employee("Сергеев", "Яков", "Михайлович", 60, "Главный инженер",
    #               200000)
    args = parser.parse_args()
    print(args)
    e1 = Employee(args.ln, args.n, args.p, args.age, args.pos, args.sal)

    print(e1)
    print(e1.get_salary())
    e1.raise_salary(10)
    print(e1.get_salary())
    print(e1.get_age())
    e1.birthday()
    print(e1.get_age())
