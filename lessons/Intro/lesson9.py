# Разбор домашнего задания

# def modify_sting_and_print(my_string: str, symbol='*', number=3):
#     my_string = f"{symbol * number}{my_string}{symbol * number}"
#     print(my_string)
#     return my_string
#
#
# modify_sting_and_print('Some string', '2', 5)
# modify_sting_and_print('Some string')
# modify_sting_and_print('Some string', 5)
# modify_sting_and_print(symbol='.', my_string='Some string', number=5)

# значения по умолчанию - def modify_sting_and_print(my_string: str, symbol='*', number=3):
# 1) АРГУМЕНТЫ ПЕРЕДАЮТСЯ ПОЗИЦИОННО! ПЕРЕДАЮТСЯ КАК КОРТЕЖ!
# 2) аргументы могут передаваться с ключами - modify_sting_and_print(symbol='.', my_string='Some string', number=5)
# => словарь!
# 3) В начале позиционные аргументы, затем именованные

# def create_lines_above_under_string(my_string, symbol='*'):
#     len_str = len(my_string)
#     add_str = symbol * len_str
#     new_sft = f'{add_str}\n{my_string}\n{add_str}'
#     print(new_sft)
#
#
# create_lines_above_under_string('Some str', '#')
# # теперь композиция из функций
# mod_str = modify_sting_and_print('Some string')
# create_lines_above_under_string(mod_str)

# def modify_sting(my_string: str, symbol='*', number=3):
#     my_string = f"{symbol * number}{my_string}{symbol * number}"
#     return my_string
#
# def print_modified_string(my_string: str, symbol='*', number=3):
#     print(modify_sting(my_string, symbol=symbol, number=number))
#
# def print_lines_above_under_string(my_string, symbol='*', modificate=False):
#     if modificate:
#         my_string = modify_sting(my_string, symbol=symbol)
#     len_str = len(my_string)
#     add_str = symbol * len_str
#     new_sft = f'{add_str}\n{my_string}\n{add_str}'
#     print(new_sft)
#
# print_modified_string('Some string')
# print_lines_above_under_string('Some string_2', modificate=True)

# def my_function(*args, **kwargs):
#     for val in args:
#         print(val)
#     print(args)
#     print(kwargs)
#
# my_function(1,'42342', (1, 2, 3), [1, 2, 3], **{'wer': 1, 'werwe': 4}, qwe=1, sqd=4)

# arg - аргументы, *args - любое количество аргументов
# kwargs - key word аргументы - именовванные аргументы

# РАБОТА С ФАЙЛАМИ
# файл - объект, пайтон работает с файлами, как с объектами

# file = open('utils.py', 'r')
# lines = file.read()
# print(lines)
# file.close()

# open --> close
# менеджер контекста with
# with open('utils.py', 'r') as file:
#     lines = file.read()
#     print(lines)
#
# with open('util.py', 'w') as file:
#     file.write('Hello!\n')
#     file.writelines('dasdasd')
#     file.writelines(lines)

# создать папку, если ее нет
import os
import shutil
#
# def create_folder(path):
#     try:
#         os.mkdir(path)
#     except FileExistsError:
#         pass
#
# create_folder('123')

# написать алфавит
def save_file(filename, path, data):
    filename_with_path = os.path.join(path, filename)
    with open(filename_with_path, 'w') as file:
        file.write(data)

alpha = [chr(number) for number in range(ord('a'), ord('z') + 1)]
alpha = ''.join(alpha)

save_file('alpha.txt', 'tmp', alpha)

# в папку поместить алфавит.txt, в который запистаь этот алфавит
# в папку поместить файлы вида a.txt, b.txt, c.txt -> z.txt, в каждый из которой букву заменить на заглавную

for symbol in alpha:
    save_file(f'{symbol}.txt', 'tmp', alpha.replace(symbol, symbol.upper()))

# случайным образом удалить половину файлов в 123
tmp_folder = os.listdir('tmp')
print(tmp_folder)

for file in list(set(tmp_folder))[:len(tmp_folder)//2]:
    os.remove(os.path.join('123', file))






