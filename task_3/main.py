"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml
from yaml.loader import SafeLoader

item = input("Введите наименование товара: ")
price = input("Введите цену товара в €: ") + "€"

with open("file.yaml") as f:
    f_content = yaml.load(f, Loader=SafeLoader)
    f_content["items"].append(item)
    f_content["items_price"][item] = price
    f_content["items_quantity"] = len(f_content["items"])

with open("file.yaml", "w") as f:
    yaml.dump(f_content, f, default_flow_style=False, allow_unicode=True)

with open("file.yaml") as f:
    f_content = yaml.load(f, Loader=SafeLoader)
    print(f_content)
