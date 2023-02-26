"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import sys
import subprocess
import chardet


try:
    a = int(input('Введите "1" для yandex.ru или "2" для youtube.com: '))
except ValueError:
    print("Вы ввели неверное значение")
    sys.exit()

if a == 1:
    ARGS_1 = ["ping", "yandex.ru"]
elif a == 2:
    ARGS_1 = ["ping", "youtube.com"]
else:
    print("Вы ввели неверное значение")
    sys.exit()

with subprocess.Popen(ARGS_1, stdout=subprocess.PIPE) as S_PING:
    print(S_PING.stdout)
    for line in S_PING.stdout:
        res = chardet.detect(line)
        print(line.decode(res['encoding']))
