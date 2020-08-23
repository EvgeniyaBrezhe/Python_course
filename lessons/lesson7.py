# СЛОВАРИ, МОДУЛИ, ФУНКЦИИ

# словари нужны для того, чтобы создавать читаемые структуры данных
# представим, что есть точка с координатами А (1;2), B (-2;4) и C(0;-6)
# ПОЗИЦИОННОЕ ИСПОЛЬЗОВАНИЕ

# 1) не меняются
# points_tuple = ((1, 2), (-2, 4), (0, -6))
# print(points_tuple[0])

# 2а) меняются (частично)
# points_list = [(1, 2), (-2, 4), (0, -6)]
# print(points_list[0])

# 2б) меняются
# points_list_change = [[1, 2], [-2, 4], [0, -6]]
# print(points_list_change[0])

# ОБРАЩЕНИЕ ПО ИМЕНИ
# points_dict = {'A': (1, 2), 'B': (-2, 4), 'C': (0, -6)}
# print(points_dict['A'])

# если нужно обратиться отдельно к иксу, а отдельно к игреку
# points_dict_spec = {'A': {'x': 1, 'y': 2}, 'B': {'x': -2, 'y': 4}, 'C': {'x': 0, 'y': -6}}
# print(points_dict_spec['A']['x'])
# если такой точки не существует - KeyError
# point_d = (3, 5)
# points_dict['D'] = point_d
# points_dict.update({'D1': 0})

# d2 = {'D2': 0}
# points_dict.update(d2)

# print(points_dict)
# если есть ключ D2, то не пропустить, а если нет - добавить в словарь по ключу D2
# test_point = (5, 7)
# if points_dict['D2']:
#     print('qwe')

# ОЧЕНЬ ПЛОХО ТАК!
# test_point = (5, 7)
# try:
#     points_dict['D2']
# except KeyError:
#     points_dict['D2'] = test_point
# print(points_dict)
# МЫ НЕ ИСПОЛЬЗУЕМ TRY-EXCEPT ДЛЯ ЛОГИКИ!

# print(points_dict.get('D2'))
# <- None

# if points_dict.get('D2') is not None:
#     print('Такой ключ есть')
# else:
#     points_dict['D2'] = test_point
# print(points_dict)

# но вообще лучше наоборот строить if
# if points_dict.get('D2') is None:
#     points_dict['D2'] = test_point
# print(points_dict)
# value = points_dict['A']
# print(value)
# get возвращает значение по ключу, если оно есть и None, если нет ключа

# for key in points_dict:
#     print(key, points_dict[key])
# значения и значения можно кинуть в список
# print(list(points_dict.keys()))
# print(list(points_dict.values()))

# МОДУЛИ (библиотеки) - возможности языка, которые реализованы другими программистами
# есть встроенные, есть внешние
# docs.python.org/3/library
