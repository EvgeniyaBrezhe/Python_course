import os


# Написать функции (и дать им названия, отражающие то, что они делают) со следующим функционалом:
# 1) функции передаем полный путь к файлу в виде строки в формате "./path/to/file/filename.ext",
# где точка означает текущую директорию.
# (Это универсальный способ задать путь. Пользователи виндовс можете почитать это:
# https://stackoverflow.com/questions/2953834/windows-path-in-python)
# Функция возвращает два параметра: название файла и путь к папке.
# Пример использования:
# filename, folder_path = first_function(path)

def get_file_name_and_path_to_folder(my_path):
    folder_path = os.getcwd()
    file_name = os.path.basename(my_path)
    return file_name, folder_path


my_file_name, my_folder_path = get_file_name_and_path_to_folder('./123/123_1.py')
print(my_file_name, my_folder_path)

###################################

# 2) функции передаем полный путь к папке в виде строки в формате "./path/to/folder",
# где точка означает текущую директорию.
# Функция возвращает список ФАЙЛОВ из этой папки. Т.к. listdir возвращает файлы и подпапки,
# то такой функционал иногда нужен.
# Напомню, что есть метод os.path.isfile(path) который возвращает True, если path указывает на файл.
# И обратите внимание на "Щелчек Таноса" из классной работы. Мы там склеиваем путь с помощью os.path.join()
# Пример использования:
# files = second_function(path)
# Значение по умолчанию - текущая папка. Т.е. second_function() вернет файлы из текущей папки.


def get_all_files_from_folder(my_path):
    files_and_folders = os.listdir(my_path)
    all_files = [value for value in files_and_folders if os.path.isfile(os.path.join(my_path, value)) is True]
    return all_files


my_files = get_all_files_from_folder('./123')
print(my_files)

###################################

# 3) функции передаем полный путь к папке в виде строки в формате "./path/to/folder",
# где точка означает текущую директорию.
# Функция возвращает СЛОВАРЬ в формате: {"files": [список ФАЙЛОВ из папки], "folders": [список ПОДПАПОК из папки]}.
# Пример использования:
# path_dict = third_function(path)
# Значение по умолчанию - текущая папка. Т.е. third_function() вернет словарь с файлами и подпапками из текущей папки.

def create_dict_with_files_and_folders(my_path='.'):
    files_and_folders = os.listdir(my_path)
    all_files_list = []
    all_folders_list = []
    for value in files_and_folders:
        if os.path.isfile(os.path.join(my_path, value)):
            all_files_list.append(value)
        else:
            all_folders_list.append(value)
    my_dict = {'files': all_files_list, 'folders': all_folders_list}
    return my_dict


my_dictionary = create_dict_with_files_and_folders('./tmp_tmp')
print(my_dictionary)

###################################
# 4) функции передаем полный путь к папке в виде строки в формате "./path/to/folder",
# где точка означает текущую директорию.
# Функция создает пустые папки в данной директории по следующему правилу:
# - если в этой директории нет подпапок - создает папку '123'
# - если в этой директории есть подпапки - создает папки в названии которых дописываем '_tmp'.
# Пример. Есть подпапка 'test'. значит создаем 'test_tmp'
#
# P.S. Данные функции никак не обрабатывают ошибки существования файлов.
# Т.е. если пользователь передаст путь к несуществующему файлу или папке - он получит ошибку пайтона.

def create_or_change_folder(my_path):
    list_of_folders = []
    for directories, folders, files in os.walk(my_path):
        list_of_folders += folders
        break
    if len(list_of_folders) == 0:
        os.mkdir('tmp')
    else:
        for folder in list_of_folders:
            os.rename(folder, str(folder) + str('_tmp'))


create_or_change_folder('.')
