# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.
import random

my_list_1 = []
for number in range(20):
    my_list_1.append(random.randint(1, 100))
print(my_list_1)

my_list_2 = [random.randint(1, 100) for number in range(20)]
print(my_list_2)

############################################

# 2) Создать словарь triangle в который записать точки A B C, и их координаты (кортежи) ,
# созданные случайным образом с помощью модуля random.
def point():
    return random.randint(-10, 10)


triangle = {'A': (point(), point()),
            'B': (point(), point()),
            'C': (point(), point())}
print(triangle)

############################################

# 3) Создать функцию my_print, которая принимает строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***
def my_print(string):
    print(f"***{string}***")


my_string = "I'm also the string"
my_print(my_string)

############################################

# 4)Создать функцию my_print, которая принимает строку и печатает ее
# с символами * НАД и ПОД строкой. КОЛИЧЕСТВО СИМВОЛОВ * РАВНО КОЛИЧЕСТВУ СИМВОЛОВ В СТРОКЕ
# Пример:
# my_str = 'I'm the string'
# Печатает
# **************
# I'm the string
# **************
def my_print(string):
    print('*' * len(string))
    print(string)
    print('*' * len(string))


my_string = "I'm also the string"
my_print(my_string)

############################################

# 5) То же, что 4, но ответ должен выглядеть так:
# ********************
# ***I'm the string***
# ********************
def my_print(string):
    middle_string = f"***{string}***"
    print('*' * (len(middle_string)))
    print(middle_string)
    print('*' * (len(middle_string)))


my_string = "I'm also the string"
my_print(my_string)
