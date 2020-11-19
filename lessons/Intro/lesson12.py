import random
import re
import json
# ЭТИМ МОЖНО БЫЛО ЗАМЕНИТЬ CHOICE ИЗ ДОМАШКИ
# def first_function():
#     print('1111111')
#
# def second_function():
#     print('222222')
#
# def third_function():
#     print('333333')
#
# func_dict = {
#     1: first_function,
#     2: second_function,
#     3: third_function
# }
#
# rand_value = random.randint(1, 3)
# func_dict[rand_value]()

# ФУНКЦИОНАЛЬНОЕ ПРОГРАММИРОВАНИЕ - одна из парадигм программирования, наряду с ооп

# LAMBDA агрументы: выражение, класс - функция - НЕ нужна, когда действию НУЖНО ДАТЬ имя
# key = lambda x:x.get('age' = obj.get('age'))

# FILTER - тип класс фильтр, передаем функцию (логика, с помощью которой она фильтруется) и итерируемый объект
# my_list = list(filter(функция, итерируемый объект))
# функция -> bool

# MAP(функция, итерируемый объект) - тип - класс мап
# my_list = list(map(функция, итерируемый объект))

# REDUCE - (функция, инетрируемый объект, [нач значение]) - функция двух аругментов - накопитель и элемент

# ----------------------

# Библиотека Requests
import requests

url = 'https://www.google.com.ua/'
response = requests.get(url=url)
# response = requests.post(url=url)

# get - получить ответ, базовый параметр - url
# post - сообщить/отправить что-то

# <Response [200]> - все хорошо, я тебе все отдал <- get
# Или Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known

# <Response [405]> <- post
# print(response.status_code)
# print(response.headers)
# print(response.encoding)
# print(response.text)
print(response.json)







