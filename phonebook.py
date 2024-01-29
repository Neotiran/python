import os

def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    with open(filename, 'r+t', encoding="utf-8") as data:
        lines_count = len(data.readlines())
        data.write(f"{lines_count + 1};{name};{phone}\n")

def read_all(filename) -> str:
    """
    Возвращает все содержимое телефоной книги.
    """
    with open(filename, 'r', encoding="utf-8") as data:
        result = data.read()    
    return result

def search_user(user: str, filename: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, 'r', encoding="utf-8") as data:
        text = data.readlines()
    res = [item for item in text if user.lower() in item.lower()]
    return '\n'.join(res).replace(';', ' ') if res else 'Вхождений не найдено'


def check_directory(filename: str):
    if filename not in os.listdir():
        with open(filename, 'w', encoding="utf-8") as data:
            data.write("")   

def copy_line(source_file:str, destination_file:str, line_number:int):
    with open(source_file, 'r', encoding="utf-8") as source:
        lines = source.readlines()
        if line_number <= len(lines):
            line_to_copy = lines[line_number - 1]

            with open(destination_file, 'a', encoding="utf-8") as destination:
                destination.write(line_to_copy)
            print(f"Строка {line_number} успешно скопирована из {source_file} в {destination_file}.")
        else:
            print("Неверный номер строки.")

INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - копирование строки из одного файла в другой
5 - завершить программу
"""
INFO_USER = "Введите имя пользователя: "
INFO_PHONE = "Введите телефон пользователя: "
INFO_SEARCH = "Введите строку для пользователя: "
INFO_SOURCE_FILE = "Введите имя исходного файла: "
INFO_DESTINATION_FILE = "Введите имя файла назначения: "
INFO_LINE_NUMBER = "Введите номер строки для копирования: "

DATA_SOURCE = 'phone.txt'
check_directory(DATA_SOURCE)

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(DATA_SOURCE))
    elif mode == 2:
        user = input(INFO_USER)
        phone = input(INFO_PHONE)
        add_new_user(name=user, phone=phone, filename=DATA_SOURCE)
    elif mode == 3:
        user = input(INFO_SEARCH)
        print(search_user(user, DATA_SOURCE))
    elif mode == 4:
        source_file_name = input(INFO_SOURCE_FILE)
        destination_file_name = input(INFO_DESTINATION_FILE)
        line_number_to_copy = int(input(INFO_LINE_NUMBER))
        check_directory(source_file_name)
        check_directory(destination_file_name)
        copy_line(source_file=source_file_name, destination_file=destination_file_name, line_number=line_number_to_copy)
    elif mode == 5:
        exit()
