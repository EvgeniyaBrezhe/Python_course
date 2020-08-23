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


def sum_numbers(text: str) -> int:
    my_list = text.split(" ")
    my_sum = 0
    for value in my_list:
        if value.isdigit():
            my_sum += int(value)
    return my_sum


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
