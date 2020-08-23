#
# my_list = ['a', 'b', 'c']
# for index in range(0, len(my_list)):
#     print(index, my_list[index])
# # <- вывод индекса и значения
# # в python есть возможность сразу получить индекс и значения через enumerate
#
# for index, value in enumerate(my_list):
#     print(index, value)
# # кортеж, который на лету распаковывается и сохраняется в переменные
#
# for enum_value in enumerate(my_list):
#     print(enum_value)
# кортеж, который можно распаковать

# дан список чисел, возвести в квадрат числа, стоящие на четных местах и оставить без изменения числа на нечетных местах
# my_list = [1, 3, 5, 7, 9]
# for index, value in enumerate(my_list):
#     if index % 2:
#         print(value)
#     else:
#         print(value ** 2)

# так, на ниже, делать нельзя, это уже true или false!
# if index % 2 == 1:

# my_list_str = ['10', '1', '21', '3', '4', '5', '6']
# my_list_int = []
#
# for value in my_list_str:
#     my_list_int.append(int(value))
#
# print(my_list_int)

#  ГЕНЕРАТОР СПИСКОВ - создание списков
#  есть результат выполнения функции
# my_list_str = ['10', '1', '21', '3', '4', '5', '6']
# my_list_int = [int(value) for value in my_list_str]
# на лету сгенерировали список - что будет попадать, что мы генерируем, сколько этих желементов, откуда будут браться данные
# print(my_list_int)
# хочу, чтобы был список, где будут квадраты этих значений
# sqr_list = [val ** 2 for val in my_list_int]
# что делаем и для каких значений
# print(sqr_list)
# нет результата выполнения функции
# [print(qwe) for qwe in sqr_list]
# это не имеет смысла
# result = [print(qwe) for qwe in sqr_list]
# print(result)
# тип none состоит из одного элемента non, это - ничего
# а как же намечатать число, которое больше, чем 20?
# my_list_str = ['10', '1', '21', '3', '43', '5656', '684', '235245']
# my_list_int = []
#
# for value in my_list_str:
#     my_list_int.append(int(value))
#     if int(value) > 20:
#         print(value)
#
# print(my_list_int)

# my_list_int = [int(value) for value in my_list_str if int(value) < 20]
# print(my_list_int)

# my_list_int = [int(value) for value in my_list_str if 2 <= len(value) <= 3]
# print(my_list_int)

# МНОЖЕСТВА {}
str_ = 'qwerty not QWERTY'

# print(list(str_))
# print(set(str_))
# преобразование списка/строки/кортежа, берет все его элементы, выбирает уникальные
# _ - Порядок - Изменяемость -
# List - + - Да, можно менять
# Tuple - + - Нет, нельзя
# Set - - - Да, можно

# my_set = set(str_.lower())
# print(len(my_set))
#
# for value in my_set:
#     print(value)

# str_1 = 'qwerty'
# str_2 = 'rewrqwerq2'
# set_1 = set(str_1)
# set_2 = set(str_2)
# intersection - пересечения, есть в обеих строках
# print(set_1.intersection(set_2))
# union - показывет все - создаются новые объекты! - просто в принте вывелся и потом будет зачищен
# print(set_1.union(set_2))
# set_1.update(set_2)
# print(set_1)
#
# my_list = [1, 2, 3, 1, 2, 3, 1, 2, 3]
# new_list = list(set(my_list))
# print(new_list)
#
# qwe = {1}
# print(qwe, type(qwe))

# my_str = 'dfgjha;ke5utauep5rgb9fvdfvz'
#
# for value in set(my_str):
#     print(f'{value}: {my_str.count(value)}')

#  СЛОВАРЬ - dict

# _ - Порядок - Изменяемость -
# List - + - Да, можно менять
# Tuple - + - Нет, нельзя
# Set - - - Да, можно
# Dict -
# ключом может быть любой неизменяемый объект, значение - любым, даже None
# my_dict = {'key_1': "123",
#            "key_2": '456',
#            5: 'qwe'}
# print(my_dict)
# print(my_dict[5], my_dict['key_2'])
# print(my_dict[2])

person = {"name": "Zhenya",
          "age": "28",
          "address": {
            'city': 'Dnipro',
            'street': 'Vasilievskaya'
          }}
print(person['name'], person['address']['city'])
person["LastName"] = 'Brezhe'
print(person['LastName'])
person["address"]['building'] = '119a'
print(person)
