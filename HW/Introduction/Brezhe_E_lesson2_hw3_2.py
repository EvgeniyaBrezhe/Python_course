# # Задание 3. (20 из 100)
# Написать программу, которая считывает введенный месяц года (в виде числа или строки, например 04 или Апрель) и выводит количество дней в этом месяце.
value = input("Введи название или номер месяца: ")

if value == "Январь" or value == "Март" or value == "Май" or value == "Июль" or value == "Aвгуст" or value == "Октябрь"or value == "Декабрь":
    print("31")
elif value == "Апрель" or value == "Июнь" or value == "Сентябрь" or value == "Ноябрь":
    print("30")
elif value == "Февраль" or value == "02":
    print("28 или 29")
elif (0 < int(value) < 8 and int(value) % 2 == 1) or int(value) == 8 or (8 < int(value) <= 12 and int(value) % 2 == 0):
    print("31")
elif (0 < int(value) < 8 and int(value) % 2 == 0) or (8 < int(value) <= 12 and int(value) % 2 == 1):
    print("30")