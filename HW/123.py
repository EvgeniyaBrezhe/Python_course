import random
import string
import re
#
# # def id_generator():
# #     return ''.join(random.choice(string.ascii_letters + string.digits + " " + string.punctuation) for value in range(random.randint(100, 1000)))
# #
# #
# #
# # print(id_generator())
#
# import json  # модуль работы с форматом json
#
# my_dict = {"name": 'John', "age": 30}
#
# my_json = json.dumps(my_dict)  # преобразует словарь в строку. dumps - dump string
# print(my_json, type(my_json))
# print('---------------------------------')
#
# # my_json = json.dumps(my_dict, indent=2)  # indent форматирует вид СТРОКИ!!!.
# # print(my_json)
# # print(type(my_json))
#
# print('---------------------------------')
# my_dict_2 = json.loads(my_json)  # преобразует строку в словарь. loads - load string
# print(my_dict_2, type(my_dict_2))
#
# print('---------------------------------')
# outfile = "lesson10/new.json"   # имя файла
# data = my_dict          # данные для записи в файл
#
# # with open(outfile, 'w') as json_file:
# #     json.dump(data, json_file)      # dump - dump object
#
# with open(outfile, 'r') as json_file:
#     data = json.load(json_file)     # load - load object
# print(data, type(data))

# length_of_m_list = random.randint(3, 10)
# print(length_of_m_list)

# def sort_key(value_dict):
#     current_value_dict = value_dict['name']
#     my_list = current_value_dict.split(" ")
#     my_new_str = my_list[len(my_list) - 1]
#     # return value_dict['name']
#     return my_new_str


# persons = [{'name': 'Joh1231asdan124 2342 2342 234234 23423 3434 34343  Alfa', 'age': 20},
#            {'name': 'Alm1231a Beta', 'age': 21},
#            {'name': 'Hen1231drick Gamma', 'age': 19}]
#
# str_1 = '4wrtb34qvj3hbq3itq35t'
# str_2 = persons[0]
# str_3 = str_2['name']
# print(str_3, type(str_3))
# date = re.findall(r'[0-9]{3,4}', str_3)
# print(date)
# some_str = '1231 22 2233 f sdfsd sdg BC 1212 222 '
# date = re.findall(r'[0-9]{3,4}', some_str)
# print(date)
# if some_str.find('BC') == -1:
#     print('no')
# else:
#     print('yes')


# for index in range(len(persons)):
#     my_dict_value = persons[index]
#     my_value = my_dict_value.get('name')
#
#     print(my_value)
#
#
# print(len(persons))
# new_persons = sorted(persons, key=sort_key)
# print(new_persons)

# a = 'Hendrick Gamma'
# b = a.split(" ")
# my_list = b[len(b) - 1]
# print(my_list)

# my_list = [
#     {"name": "Brahmagupta",
#      "years": "597 – 668."},
#     {"name": "Rene Descartes",
#      "years": "1596 – 1650."},
#     {"name": "Euclid",
#      "years": "c. 325 – c. 270 BC."}]
#
# year_1 = my_list[0]
# year_2 = my_list[1]
# year_3 = my_list[2]
# print(year_1, year_2, year_3, type(year_3))
# print('year_1')
#
# year_from_dict_1 = year_1['years'].split('-')
# year_from_dict_2 = year_2['years'].split('-')
# year_from_dict_3 = year_3['years'].split('-')
# print(year_from_dict_1, year_from_dict_2, year_from_dict_3, type(year_from_dict_3))
# print('year_from_dict_1')
#
# str_years_1 = str(year_from_dict_1)
# str_years_2 = str(year_from_dict_2)
# str_years_3 = str(year_from_dict_3)
# print(str_years_1, str_years_2, str_years_3, type(str_years_3))
# print('str_years_1')
#
# place_1 = str_years_1.find('–')
# place_2 = str_years_2.find('–')
# place_3 = str_years_3.find('–')
# print(place_1, place_2, place_3)
#
# str_death_1 = str_years_1[place_1:len(str_years_1)]
# str_death_2 = str_years_2[place_2:len(str_years_2)]
# str_death_3 = str_years_3[place_3:len(str_years_3)]
# print(str_death_1, str_death_2, str_death_3)
#
# date_1 = int(re.findall(r'\d+', str_years_1)[1])
# date_2 = int(re.findall(r'\d+', str_years_2)[1])
# date_3 = int(re.findall(r'\d+', str_years_3)[1])
# print(date_1, date_2, date_3, type(date_3))
#
# print('-----------')
# if 'BC' not in str_death_1:
#     end_date_1 = date_1
# else:
#     end_date_1 = date_1 * - 1
#
# print(end_date_1, type(end_date_1))
#
# if 'BC' not in str_death_2:
#     end_date_2 = date_2
# else:
#     end_date_2 = date_2 * - 1
#
# print(end_date_2)
#
# if 'BC' not in str_death_3:
#     end_date_3 = date_3
# else:
#     end_date_3 = date_3 * - 1
#
# print(end_date_3)

line = "Fibonacci’s Book"
count = len(re.findall(r'[a-zA-z’]+', line))
print(count)




