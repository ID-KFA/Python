"""
Реализовать консольное приложение заметки, с сохранением, чтением, добавлением,
редактированием и удалением заметок. Заметка должна содержать идентификатор,
заголовок, тело заметки и дату/время создания или последнего изменения заметки.
Сохранение заметок необходимо сделать в формате json или csv формат (разделение
полей рекомендуется делать через точку с запятой). Реализацию пользовательского
интерфейса студент может делать как ему удобнее, можно делать как параметры
запуска программы (команда, данные), можно делать как запрос команды с
консоли и последующим вводом данных, как-то ещё, на усмотрение студента.

Приложение должно запускаться без ошибок, должно уметь сохранять данные в файл,
уметь читать данные из файла, делать выборку по дате, выводить на экран
выбранную запись, выводить на экран весь список записок, добавлять записку,
редактировать ее и удалять.

"""

import csv
import datetime


def main():
    """
    Main menu
    """
    choice = None

    while choice != '0':
        print("""
        Notes

        0 - Quit
        1 - Show all notes
        2 - Add note
        3 - Edit note
        4 - Delete note
        5 - Search note
        
        """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Goodbye!")

        elif choice == "1":
            show_notes()

        elif choice == "2":
            add_note()

        elif choice == "3":
            edit_note()

        elif choice == "4":
            del_note()

        elif choice == "5":
            search_note()

        else:
            print("\nSorry, but", choice, "isn't a valid choice.")


def add_note():
    """
    Add note
    """
    id_note = input("Id: ")
    try:

        with open("notes.csv", "r", encoding="utf-8") as file:
            f_reader = csv.reader(file, delimiter=';')

            for row in f_reader:
                if row[0] == id_note:
                    print(f"Id {id_note} is already taken")
                    return

    except:
        print("Error checking Id")

    caption = input("Caption: ")
    note = input("Note: ")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    try:
        with open("notes.csv", "a", encoding="utf-8") as file:
            f_writer = csv.writer(file, delimiter=';')
            f_writer.writerow([id_note, caption, note, now])
            print("Done")
    except:
        print("Error adding note")

def show_notes():
    """
        Show all notes
        """
    try:
        with open("notes.csv", "r", encoding="utf-8") as file:
            f_reader = csv.reader(file, delimiter=';')
            for row in f_reader:
                print(
                    f" Id: {row[0]}, Caption: {row[1]}, Text: {row[2]}, "
                    f"Date: {row[3]}")
    except:
        print("Error showing all notes")


def del_note():
    """
    Delete note by Id
    """
    id_note = input("What Id you want to delete? ")
    try:
        with open("notes.csv", "r", encoding="utf-8") as file:
            f_reader = csv.reader(file, delimiter=';')
            rows = list(f_reader)

            for i in range(len(rows)):
                if rows[i][0] == id_note:
                    del rows[i]
                    break

        with open("notes.csv", "w", encoding="utf-8") as file:
            f_writer = csv.writer(file, delimiter=';')

            f_writer.writerows(rows)
            print("Done")

    except:
        print("Error deleting note")


def edit_note():
    """
    Edit note by Id
    """
    id_note = input("What Id you want to edit? ")
    try:
        with open("notes.csv", "r", encoding="utf-8") as file:
            f_reader = csv.reader(file, delimiter=';')
            rows = list(f_reader)

            for i in range(len(rows)):
                if rows[i][0] == id_note:
                    caption = input("Enter new caption: ")
                    note = input("Enter new note: ")
                    now = datetime.datetime.now().strftime(
                        "%Y-%m-%d %H:%M")

                    rows.append([id_note, caption, note, now])

                    del rows[i]

                    break

        with open("notes.csv", "w", encoding="utf-8") as file:
            f_writer = csv.writer(file, delimiter=';')

            f_writer.writerows(rows)
            print("Done")

    except:
        print("Error editing note")


def search_note():
    """
    Search note by date
    """
    date = input("Enter the date in format Year-month-day: ")
    try:
        with open("notes.csv", "r", encoding="utf-8") as file:
            f_reader = csv.reader(file, delimiter=';')
            for row in f_reader:
                if row[3].startswith(date):
                    print(
                        f" Id: {row[0]}, Caption: {row[1]}, Text: {row[2]},"
                        f" Date: {row[3]}")

    except:
        print("Error searching note")


main()
