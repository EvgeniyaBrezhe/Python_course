# 1.
# Дана строка my_str и пустой список my_list.
# Заполнить my_list символами из my_str, которые стоят на четных местах в строке
# my_str = 'wrwerwfrFEW'
# my_list = []
# # print(id(my_list))
# # my_list += list(my_str[::2])
# # print(id(my_list))
#
# #  ИЛИ
# for symbol in my_str[::2]:
#     my_list.append(symbol)
# print(my_list)

# 2.
# Дана строка my_str, список str_index целых чисел в диапазоне от 0 до длинны строки, пустой список my_list.
# Заполнить my_list символами из my_str, которые стоят на местах с индексами из str_index
# my_str = 'qwerty'
# str_index = [1, 3, 5, 4, 5, 3, 2, 1]
# my_list = []
#
# for index in str_index:
#     my_list.append(my_str[index])
# print(my_list)

# 3.
# Даны списки my_list_1 и my_list_2.
# Создать список my_result в который поместить элементы из my_list_1 и my_list_2 через один.
# а) количество элементов одинаковое
# б) количество элементов разное

# for value in range(5): ИЛИ range (2,10) ИЛИ range (2,10,2)
# print (value)
# my_list_1 = [1, 2, 3, 4, 5, 6]
# my_list_2 = ['q', 'w', 'e', 'r', 't', 'y']
# my_result = []
#
# for index in range(len(my_list_1)):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
# print(my_result)

# my_list_1 = [1, 2, 3, 4, 5, 6]
# my_list_2 = ['q', 'w', 'e', 'r', 't', 'y']
# my_result = []
# if len(my_list_1) == len(my_list_2):
#     for index in range(len(my_list_1)):
#         my_result.append(my_list_1[index])
#         my_result.append(my_list_2[index])
# else:
#     pass
# print(my_result)

# my_list_1 = [1, 2, 3, 4]
# my_list_2 = ['q', 'w', 'e', 'r', 't', 'y']
# my_result = []
# if len(my_list_1) == len(my_list_2):
#     for index in range(len(my_list_1)):
#         my_result.append(my_list_1[index])
#         my_result.append(my_list_2[index])
# elif len(my_list_1) > len(my_list_2):
#     for index in range(len(my_list_2)):
#         my_result.append(my_list_1[index])
#         my_result.append(my_list_2[index])
#     # my_result += my_list_1[len(my_list_2):]
#     my_result.extend(my_list_1[len(my_list_2):])
#     # my_result.append(my_list_1[len(my_list_2):])
# else:
#     # if len(my_list_1) < len(my_list_2):
#     # my_list_1, my_list_2 = my_list_2, my_list_1
#     for index in range(len(my_list_1)):
#         my_result.append(my_list_1[index])
#         my_result.append(my_list_2[index])
#     my_result.extend(my_list_2[len(my_list_1):])
# print(my_result)

# 4.
# Даны списки my_list_1 и my_list_2.
# Создать список my_result в который поместить четные элементы из my_list_1 и нечетные элементы из my_list_2 -> на дом

# 5.
# Дано целое число. Определить сколько цифр в этом числе.
# value = input("Введи число")
# print(len(value))

# 6.
# Дано целое число. Определить наибольшую цифру в этом числе.
# value = input("Введи число")
# print(max(value))

# 7.
# Дано целое число. Составить число с цифрами в обратном порядке.
# number = str(123124)
# print(int(number[::-1]))

# 8.
# Дано целое число. Составить число с цифрами в порядке возрастания.
# Сортировка списков - может сортировать только изменяемые объекты, строки и кортежи нельзя сортировать, но их можно легко перегнать в список!
# внутренняя сортировка -> my_list.sort() - она меняет объект!
# внешняя сортировка -> если нужен тот, который был - new_list = sorted(my_list)
# number = [1, 2, 3, 1, 2, 4]
# number.sort()
# print(number)

number = [1, 2, 3, 1, 2, 4]
print(sorted(number))