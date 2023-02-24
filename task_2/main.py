"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""
import json


def write_order_to_json():
    """Записывает информацию в json файл"""

    item = input("Введите наименование товара: ")
    quantity = input("Введите количество товара: ")
    price = input("Введите цену товара: ")
    buyer = input("Введите имя покупателя: ")
    data = input("Введите дату покупки: ")

    order = {"item": item, "quantity": quantity, "price": price,
             "buyer": buyer,
             "date": data}

    with open("orders.json") as f:
        obj = json.load(f)

    obj["orders"].append(order)

    with open("orders.json", "w") as f:
        json.dump(obj, f, sort_keys=True, indent=4)


write_order_to_json()
