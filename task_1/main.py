"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import csv
import re


def get_data():
    """ Читает информацию из txt файла и передает в список"""
    os_prod_list = []
    os_name_list = []
    os_code_list = []

    os_type_list = []
    main_data = []
    row = []

    for n in range(1, 4):
        f = open(f"info_{n}.txt", encoding="utf-8")
        data = f.read()

        os_prod_inf = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_list.append(os_prod_inf.findall(data)[0].split()[2])

        os_name_inf = re.compile(r'Windows\s*\S*')
        os_name_list.append(os_name_inf.findall(data)[0])

        os_code_inf = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(os_code_inf.findall(data)[0].split()[2])

        os_type_inf = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(os_type_inf.findall(data)[0].split()[2])
        f.close()

    header_data = ["ID", "Изготовитель системы", "Название ОС",
                   "Код продукта", "Тип системы"]
    main_data.append(header_data)

    for i in range(3):
        row.append(i + 1)
        row.append(os_prod_list[i])
        row.append(os_name_list[i])
        row.append(os_code_list[i])
        row.append(os_type_list[i])

        main_data.append(row)
        row = []

    return main_data


def write_to_csv():
    """ Создает CSV файл из списка"""
    with open("base.csv", "w", encoding="utf-8") as f:
        f_writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

        f_writer.writerows(get_data())


write_to_csv()
