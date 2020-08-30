import random
import string
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


persons = [{'name': 'John1 Alfa', 'age': 20},
           {'name': 'Alma Beta', 'age': 21},
           {'name': 'Hendrick Gamma', 'age': 19}]

# for index in range(len(persons)):
#     my_dict_value = persons[index]
#     my_value = my_dict_value.get('name')

    print(my_value)


print(len(persons))
# new_persons = sorted(persons, key=sort_key)
# print(new_persons)

# a = 'Hendrick Gamma'
# b = a.split(" ")
# my_list = b[len(b) - 1]
# print(my_list)