# # тернарный оператор (!)
# х = 10
#
# if х >= 0:
#     value_sign = '+'
# else:
#     value_sign = '-'
#  OR
# value_sign = '+' if x >= 0 else '-'
# print(value_sign)

# приведение типов
# приведение типа к bool
# value = 1
# print(bool(value))
#
# value = 0.0
# print(bool(value))
#
# value = 'True'
# print(bool(value))
#
# value = ''
# print(bool(value))

# if 'asd':
#     print('ASD')
# else:
#     print("!!!")
#
# if '':
#     print('ASD')
# else:
#     print("!!!")

# value = 'dfsdfsdf'
#
# if 12 // 2:
#     print('good')
# else:
#     print('bad')

# if (12 % 2) or 'something':
#     print('good')
# else:
#     print('bad')

#  ----------------------------

# Строки в Python
# my_str_1 = 'qwerty'
# my_str_2 = '123'
#
# print(my_str_1 + my_str_2)
# print(my_str_1 + my_str_2 * 2)
#
# # len() - длина строки (количество объектов)
# print(len(my_str_1 + my_str_2))
#
# # Форматирование строк
# name = 'Zhenya'
# age = 28.23123123
#
# # print("I am " + name + ". I am " + str(age) + " years old")
# # print(f"I am {name}. I am {age:.2f} years old.")
# print("I am",{name},"I am",{age}",years old".format(name, age)

# Оператор принадлежности

# symbol = input('Vvedi bukvu angl alphavita')
# if symbol in 'eyuioa':
#     print('eto glasnaya')
# else:
#     print('eto soglasnaya')

# Цикл for
# str - итерируемый объект

# symbol - имя для цикла, временная, не надо ее потом использовать
# for symbol in 'qwerty':
#     print(symbol)
#
# my_long_string = '123456789'
#
# for symbol in my_long_string:
#     if symbol in 'ey':
#         print(symbol)
#
# print(my_long_string[len(my_long_string) - 1])
# print(my_long_string[- 1])

# нельзя my_long_string[0] = 'R' - строка есть неизменяемый объект
# my_long_string = 'R' + my_long_string[1:10]
# если до конца - то ничего не пишем, позиция работает НЕвключительно
# my_long_string = 'R' + my_long_string[-3:-10]
# my_long_string = 'R' + my_long_string[1:10:3]
# my_long_string = 'R' + my_long_string[::3]
# # разворот строки ->
# my_long_string = 'R' + my_long_string[::-1]
# my_long_string = 'R' + my_long_string[7:3:-1]
# # ==
# my_long_string = 'R' + my_long_string[4:8]
# my_long_string = 'R' + my_long_string[::-1]
#
# print(my_long_string)

# Методы строк
# aaa() - действие, функция, метод
# my_str = 'abc012abcABC'
# my_str = my_str.upper()
# my_str = my_str.lower()
# my_str = my_str.capitalize()

# Pythonworld.ru!

# print(my_str)

# name = input('Введи свое имя: ')
#
# if name.lower() == 'иван':
#     print('yes')
# else:
#     print('no')

# www = 'www.conquer_and_command.net'
# if '.com' in www:
#     print('com in www')
# else:
#     print('com not in www')
#
# value = '123456789'
# my_str = value if len(value) <= 5 else value[2:5:2]
#
# print(my_str[::-1])

# my_str = 'My name is Vova. I am a teacher !'
#
# for symbol in my_str:
#     if symbol.isupper() and symbol.isalpha():
#         print(symbol)

# 9) У вас есть переменная my_str, тип - str. Вывести на экран все символы, которые не являются буквой или цифрой.
# my_str = 'My string __ +++ is 123456789!!! :)'
#
# for symbol in my_str:
#     if not symbol.isalnum():
#         print(symbol)
# #####################################################

my_str = "My name is Vova. I am a teacher !"
for symbol in my_str:
    if not symbol.isupper() and symbol.isalpha():
        print(symbol)