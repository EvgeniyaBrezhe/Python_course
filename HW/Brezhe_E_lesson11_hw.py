# data.json - файл с данными о некоторых математиках прошлого.
import json


# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.

def json_reader(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data


# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.

def sort_key(dict_value):
    name_from_dict = dict_value["name"]
    split_list_of_values = name_from_dict.split(" ")
    last_name = split_list_of_values[len(split_list_of_values) - 1]
    return last_name


def sort_function():
    sorted_dict = sorted(json_reader('data.json'), key=sort_key)
    print(sorted_dict)


# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.



# 4. Написать функцию сортировки по количеству слов в поле "text"
