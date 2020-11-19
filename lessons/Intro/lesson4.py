# Обработка исключений
# try:
#     value = int(input('Введи целое число'))
# except ValueError:
#     print("Что-то не так")
#     value = "" # ИЛИ value = 0
#
# print(value)
# result = 1
# try:
#     value = int(input('Введи целое число: '))
#     result = result / value
# except ValueError: # ИЛИ except (ValueError, ZeroDivisionError)
#     print("Что-то не так")
# except ZeroDivisionError:
#     print("На нуль делить нельзя")
#
# print(result)

# value = 20
# if value % 2 = 0
# else ..
#  если bool (value % 2) -> можно написать по-другому
# if not value % 2
# else..

# -------

# Кортеж (tuple) - перечисленная в скобочках последовательность элементов
# value_tup = (1,2,'3',4,5)
# print(value, type(value))
# print(value[0])
# print(value[2])
# print(value[-1])
# print(value[1:3])
# также как и строка, кортеж является НЕизменяемым типом

# a = 2
# b = 3
# qwe = (2, 3) # можно и без скобочек, но так лучше не делать - явное лучше, чем неявное
# a, b = qwe # распаковка кортежа, если бы у меня не соответствовало количество, был бы valueerror - to many values / not enough values
# print(f'a={a},b={b}')
# a, b = b, a
# print(f'a={a},b={b}')

# for val in value:
#     print(val,type(val))

# Список (list)

# my_list = [1,2,3,4,5]
# print(my_list,type(my_list))
# print(my_list[1],my_list[-1], my_list[::-1])
# my_list[2] = 'qwerty' # внутри списка можно менять значения!
# print(my_list)

# В список можно добавлять элементы!

# my_str = 'srgadhsrw hwvywgtrgtcsrve'
# result = []
# for symbol in my_str:
#     if symbol in 'eyuioa':
#         print(result)
#         result.append(symbol) # append - добавление элемента в конец списка
# print(result)
#
# result.pop()
#
# print(result)
# структура данных - стек - первый вошел, последний вышел

# aa = [1] * 5
# bb = [4,5,6]
# list_ = aa + bb
# print(list_ * 3)
# -------------------
# value_list = list(value_tup)
# print(value_list)
# поменять символ в кортеже можно через приведение к типу лист и обратно
# подводный камень - меняется объект через второе его имя - выйти из этой ситуации можно через метод "copy"
# в python есть два копирования - поверхностное (copy) и глубокое (deep copy)
# value_list_new = value_list # value_list_new = value_list.copy()
# value_list_new[2] = 3
# print(value_list_new)
# print(value_list)

# Цикл While - делай, пока правда
# count = 11
# while count > 0:
#  print("Hello!")
#  count = count - 2 # count -=1 - каунт уменьшаю на единичку

# count = 0
# while count <= 10:
#  print(f"Hello!,{count}")
#  count += 1

# count = 1
# while True:
#  print(f"Hello!,{count}")
#  count += 1
#  if count >=10:
#   break

# Задача: угадай число - c брейком

# my_value = 7
#
# while True:
#  value = int(input("Введи число от 1 до 10 включитедльно: "))
#  if value == my_value:
#   print("Угадала")
#   break
#  elif value < my_value:
#   print("Больше!")
#  else:
#   print("Меньше!")

# Задача: угадай число - c флагом

# my_value = 7
# exit_flag = True
# while exit_flag:
#  value = int(input("Введи число от 1 до 10 включитедльно: "))
#  if value == my_value:
#   print("Угадала")
#   exit_flag = False
#  elif value < my_value:
#   print("Больше!")
#  else:
#   print("Меньше!")

# ------
count = 10
exit_flag = True
while exit_flag:
 count -= 1
 if count > 0:
   exit_flag = False
 print('test')

