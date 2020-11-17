# 1. Дано целое число (int). Определить сколько нулей в этом числе.
my_number = 123000321
counter = str(my_number).count('0')
print(counter)
############################################

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.
my_number = str(12300012300)
counter = 0
for index in my_number[::-1]:
    if index == '0':
        counter += 1
    else:
        break
print(counter)
############################################

# 3. Даны списки my_list_1 и my_list_2. Создать список my_result в который вначале поместить четные элементы из my_list_1
# и потом нечетные элементы из my_list_2.
my_list_1 = [1, 2, 3, 4]
my_list_2 = [11, 22, 33, 44]
my_result = []
for index in my_list_1:
    if not index % 2:
        my_result.append(index)
for index in my_list_2:
    if index % 2:
        my_result.append(index)
print(my_result)
############################################

# 4. Дан список my_list. Создать список new_list у которого первый элемент из my_list стоит на последнем месте.
# Если my_list [1,2,3,4], то new_list [2,3,4,1]
my_list = ['a', 1, 'c', 2]
new_list = my_list.copy()
new_list.append(new_list.pop(0))
print(new_list)
############################################

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место. [1,2,3,4] -> [2,3,4,1].
# Пересоздавать список нельзя!
my_list = ['a', 1, 'c', 2]
my_list.append(my_list.pop(0))
print(my_list)
############################################

# 6. Дана строка в которой есть числа (разделяются пробелами). Например "43 больше чем 34, но меньше чем 56".
# Найти сумму ВСЕХ чисел в этой строке. Для данного примера 133.
my_string = '20 больше чем 10, но меньше чем 30'
new_str = my_string.replace(' ', ',')
my_list = new_str.split(',')
counter = 0
for index in my_list:
    if index.isdigit():
        counter += int(index)
print(counter)
############################################

# 7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен
# подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abc' -> ['ab', 'c_']
my_str = 'abcdefghi'
new_str = ''
my_list = []
if len(my_str) % 2:
    new_str = my_str + '_'
else:
    new_str = my_str
for index in range(0, len(new_str), 2):
    my_list.append(new_str[index:index + 2])
print(my_list)
############################################

# 8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit. В переменную sub_str поместить часть строки
# между этими символами. my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"
my_str = 'My_long str'
l_limit = 'o'
r_limit = 't'
l_index = my_str.find(l_limit)
r_index = my_str.find(r_limit)
sub_str = my_str[l_index + 1:r_index]
print(sub_str)
############################################

# 9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit. В переменную sub_str поместить НАИБОЛЬШУЮ часть
# строки между этими символами. my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
my_str = 'My long string'
l_limit = 'o'
r_limit = 'g'
l_index = my_str.find(l_limit)
r_index = my_str.rfind(r_limit)
sub_str = my_str[l_index + 1:r_index]
print(sub_str)
############################################

# 10. Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей (слева и справа),
# и выведите количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно
# соседей. Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
numbers = [2, 4, 1, 5, 3, 9, 0, 7]
count = 0
for index in range(1, len(numbers)-1):
    if numbers[index] > numbers[index-1] + numbers[index+1]:
        count += 1
print(count)
