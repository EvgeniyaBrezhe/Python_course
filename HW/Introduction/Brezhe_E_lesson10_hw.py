# Цель задания - создать функции, которые будут генерировать случайные данные нужного формата
# для записи в файлы разных типов.
import random
import string
import json
import csv


# Функция 1. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы, знаки препинания.
# Также необходимо обязательно использовать РОВНО 9 символов перехода на новую строку (\n) В СЕРЕДИНЕ данной строки.

def create_string_for_txt():
    my_list = []
    my_str = ""
    for value in range(random.randint(100, 1000)):
        symbol = random.choice(string.ascii_letters + string.digits + " " + string.punctuation)
        my_list.append(symbol)
    for value in range(8):
        my_list.insert(random.randint(0, len(my_list)), '\n')
    my_str = my_str.join(my_list)
    return my_str


print(create_string_for_txt())


# Функция 2. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита.
# Значения - целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1, или True/False.

def one_key():
    for value in range(5):
        symbol = ''.join(random.choices(string.ascii_lowercase, k=5))
    return symbol


def one_value():
    values_list = [random.randint(-100, 100), random.random(), True, False]
    return random.choice(values_list)


def my_dict():
    my_dictionary = {}
    for index in range(random.randint(5, 20)):
        one_pair = {one_key(): one_value()}
        my_dictionary.update(one_pair)
    return my_dictionary


print(my_dict())


# Функция 3. Создает данные для записи в файл csv.
# Создает и возвращает список длинны n внутренних списков длинны m (таблица с n строк и m столбцов).
# Числа n и m выбираются случайно в диапазоне от 3 до 10.
# В таблицу записывать значения или 0 или 1.
# Заголовка у таблицы нет.

def create_m_lists(length_of_m_list_def):
    m_list = []
    values = [0, 1]
    for value in range(0, length_of_m_list_def):
        one_list = random.choice(values)
        m_list.append(one_list)
    return m_list


def create_list_for_csv():
    list_for_csv = []
    length_of_m_list = random.randint(3, 10)
    for values in range(random.randint(3, 10)):
        list_for_csv.append(create_m_lists(length_of_m_list))
    return list_for_csv


print(create_list_for_csv())


# А теперь основное задание:
# Написать функцию file_writer которой принимает один параметр - имя файла(вместе с путем).
# В зависимости от расширения файла (txt, csv, json) сгенерировать данные для записи и записать в данный файл.
# Если расширение не соответствует заданным, то вывести ошибку "Unsupported file format"

def write_txt(filename_with_path):
    with open(filename_with_path, 'w') as txt_file:
        data = create_string_for_txt()
        txt_file.write(data)


def write_json(filename_with_path):
    with open(filename_with_path, 'w') as json_file:
        json.dump(my_dict(), json_file)


def write_csv(filename_with_path):
    data = []
    with open(filename_with_path, 'w') as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerows(create_list_for_csv())


def file_writer(filename_with_path):
    ext = filename_with_path.rsplit(".", 1)[-1]
    if ext == 'txt':
        write_txt(filename_with_path)
    elif ext == 'json':
        write_json(filename_with_path)
    elif ext == 'csv':
        write_csv(filename_with_path)
    else:
        raise Exception("Unsupported file format")


call_function = file_writer('test.txt')
