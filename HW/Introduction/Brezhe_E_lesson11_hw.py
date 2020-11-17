# data.json - файл с данными о некоторых математиках прошлого.
import json
import re


# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.

def json_reader(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data


# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.

def sort_key_last_name(dict_value):
    name_from_dict = dict_value["name"]
    split_list_of_values = name_from_dict.split(" ")
    last_name = split_list_of_values[len(split_list_of_values) - 1]
    return last_name


def sort_function_2():
    sorted_dict = sorted(json_reader('data.json'), key=sort_key_last_name)
    print(sorted_dict)


# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.


def sort_key_date(dict_value):
    years_from_dict = dict_value['years']
    dash_place = years_from_dict.find('–')
    str_death = years_from_dict[dash_place:len(years_from_dict)]
    almost_death_date = int(re.findall(r'\d+', years_from_dict)[1])
    if 'BC' not in str_death:
        death_date = almost_death_date
    else:
        death_date = almost_death_date * - 1
    return death_date


def sort_function_3():
    sorted_dict = sorted(json_reader('data.json'), key=sort_key_date)
    print(sorted_dict)


# 4. Написать функцию сортировки по количеству слов в поле "text"

def sort_key_count(dict_value):
    text_from_dict = dict_value['text']
    word_count = len(re.findall(r'[a-zA-z’]+', text_from_dict))
    return word_count


def sort_function_4():
    sorted_dict = sorted(json_reader('data.json'), key=sort_key_count)
    print(sorted_dict)
