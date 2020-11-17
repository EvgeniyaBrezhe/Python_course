# 1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
# Напечатать столько раз my_symbol, сколько он встречается в my_str.
# Пример:  my_str="blablacar", my_symbol="bla".
# Вывод на экран:
# bla
# bla
my_str = "Cat says: 'meow meow meowmeow meow meow'"
my_symbol = 'meow'
for i in range(my_str.count(my_symbol)):
    print(my_symbol)
# ИЛИ
#  count = my_str.count(my.symbol)
# print((my_symbol + "\n")) * count
# print(f"{my_symbol}\n")) * count + метод strip - убрать последний перенос строки

#####################################################

# 2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
# Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str.
# Пример:  my_str="blablacar", my_symbol="bla".
# Вывод на экран:
# 2
my_str_2 = "Cat says: 'meow meow meowmeow meow meow'"
my_symbol = my_str_2.count('meow')
print(my_symbol)
#####################################################

# 3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько РАЗНЫХ символов встречается в my_str.
# Большая и маленькая буква считается как один символ. Пробелы, запятые и т.д. считаем тоже как символы.
# Пример:  my_str="bla BLA car".
# Вывод на экран:
# 6
my_str_3 = "Ccat Ssaaaaaaays: 'Mmeow meow meow'"
new_str = ''
for i in my_str_3.lower():
    if i not in new_str:
        new_str = new_str + i # new_str += i
print(len(new_str))

