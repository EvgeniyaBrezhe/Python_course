import re
import datetime
# def easy_unpack(elements: tuple) -> tuple:
#     """
#         returns a tuple with 3 elements - first, third and second to the last
#     """
#     result = (elements[0], elements[2], elements[len(elements) - 2])
#     return result
#
#
# if __name__ == '__main__':
#     print('Examples:')
#     print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
#
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
#     assert easy_unpack((6, 2, 9, 4, 3, 9)) == (6, 9, 3)
#     assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
#     assert easy_unpack((6, 3, 7)) == (6, 7, 3)
#     print('Done! Go Check!')
# ----------------------

# def first_word(text: str) -> str:
#     """
#         returns the first word in a given text.
#     """
#     # if " " in text:
#     #     find_space = text.find(" ")
#     # else:
#     #     find_space = len(text)
#     # return text[0:find_space]
#
#     index = text.find(" ")
#     return text[:index] if index != -1 else text
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(first_word("Hello world"))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert first_word("Hello world") == "Hello"
#     assert first_word("a word") == "a"
#     assert first_word("hi") == "hi"
#     print("Coding complete? Click 'Check' to earn cool rewards!")
# -----------------------

# def is_acceptable_password(password: str) -> bool:
#     return True if len(password) > 6 else False
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(is_acceptable_password('short'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_acceptable_password('short') == False
#     assert is_acceptable_password('muchlonger') == True
#     assert is_acceptable_password('ashort') == False
#     print("Coding complete? Click 'Check' to earn cool rewards!")
#
#
# def sum_numbers(text: str) -> int:
#     my_list = text.split(" ")
#     my_sum = 0
#     for value in my_list:
#         if value.isdigit():
#             my_sum += int(value)
#     return my_sum
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(sum_numbers('hi'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert sum_numbers('hi') == 0
#     assert sum_numbers('who is 1st here') == 0
#     assert sum_numbers('my numbers is 2') == 2
#     assert sum_numbers('This picture is an oil on canvas '
#  'painting by Danish artist Anna '
#  'Petersen between 1845 and 1910 year') == 3755
#     assert sum_numbers('5 plus 6 is') == 11
#     assert sum_numbers('') == 0
#     print("Coding complete? Click 'Check' to earn cool rewards!")
# my_list = [-37,-36,-19,-99,29,20,3,-7,-64,84,36,62,26,-76,55,-24,84,49,-65,41]
# sum_of_integers = 0
#
# for number, value in enumerate(my_list):
#     if number % 2 == 0:
#         sum_of_integers += value
#
# result = sum_of_integers * my_list[len(my_list)-1]
# print(result)


# def checkio(array: list) -> int:
#     sum_of_integers = 0
#     if len(array) == 0:
#         return 0
#     if len(array) != 0:
#         for lala in array:
#             if array.index(lala) % 2 == 0:
#                 sum_of_integers += lala
#         result = sum_of_integers * array[len(array)-1]
#     return result


#
# # These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     print('Example:')
#     print(checkio([0, 1, 2, 3, 4, 5]))
#
#     assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
#     assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
#     assert checkio([6]) == 36, "(6)*6=36"
#     assert checkio([]) == 0, "An empty array = 0"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# my_sequence = ("brightness wright",)
# my_sequence_new = ",".join(my_sequence)
# result = my_sequence_new.replace("right", "left")
# print(result)

# words = "He is 123 man"
# words_new = words.split(" ")
# list_new = []
# index = 0
#
#
# for value in words_new:
#     if value.isdigit():
#         list_new.append('1')
#     else:
#         list_new.append('0')
# words_new_super = "".join(list_new)
# if "000" in words_new_super:
#     print(True)
# else:
#     print(False)

# my_string = "...,,  don't touch it..,,"
# first_word = ""
#
# my_new_string = my_string.replace(".", " ")
# my_second_string = my_new_string.replace(",", " ")
# my_list = my_second_string.split(" ")
#
# print(my_list)
#
# for index in my_list:
#     if len(index) > 0:
#         print(index)
#         break
#
#
# def first_word(text):
#     return text.replace('.', ' ').replace(',', ' ').strip().split()[0]
#
# print(first_word(my_string)
# a = (1982, 4, 15)
# b = (1982, 4, 19)
# c = abs(datetime.date(a[0], a[1], a[2]) - datetime.date(b[0], b[1], b[2]))
# # if c == "0:00:00":
# #     d = 0
# # else:
# #     d = c.split()[0]
# # print(d)
# print(c.days)

# m_string = 'Petersen between 1845 and 1910 year'
# answer = 0
# for index in m_string:
#     if index.isdigit():
#         answer += 1
#
# print(answer)

my_string = 'welcome to a game'
my_list = my_string.split()

welcome = 'welcome'
welcome_1 = welcome[::-1]


print(welcome_1)