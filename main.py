# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать
# функционал для изменения и удаления данных.

from csv import DictReader, DictWriter
from os.path import exists


def create_file():
    with open('phone.csv', 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()


def get_info():
    info = ['Иванов', 'Иван', '88002000600',
            'Петров', 'Петр', '88002000700',
            'Сидоров', 'Сидр', '88002000800']
    return info


def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    return res


def write_file(file_name, lst):
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    for i in range(0, len(lst), 3):
        obj = {'Фамилия': lst[i], 'Имя': lst[i + 1], 'Номер': lst[i + 2]}
        res.append(obj)
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(res)


def delete_data(file_name):
    surname = input('Введите фамилию удаляемого объекта: ')
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
        for el in res:
            if el['Фамилия'] == surname:
                res.remove(el)
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(res)


def change_data(file_name):
    old_surname = input('Введите фамилию, которую хотите изменить: ')
    new_surname = input('Введите новую фамилию: ')
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
        for el in res:
            if el['Фамилия'] == old_surname:
                el['Фамилия'] = new_surname
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(res)


def main():
    while True:
        command = input('Введите команду: ')
        match command:
            case 'q': break
            case 'r':
                if not exists('phone.csv'):
                    break
                print(read_file('phone.csv'))
            case 'w':
                if not exists('phone.csv'):
                    create_file()
                get_info()
                write_file('phone.csv', get_info())
            case 'd':
                if not exists('phone.csv'):
                    break
                delete_data('phone.csv')
            case 'c':
                if not exists('phone.csv'):
                    break
                change_data('phone.csv')
            case _:
                print('Неизвестная команда')


main()
