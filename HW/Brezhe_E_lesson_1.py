import random
import time
import functools
from time import sleep
# def positive_result(function):
#     def wrapper(*args, **kwargs):
#         assert result >= 0, function.__name__ + "()"
#         return result
#     wrapper.__name__ = function.__name__
#     wrapper.__doc__ = function.__doc__
#     return wrapper

# def wrapper_function():
#     def hello_world():
#         print("Hello world!")
#     hello_world()
#
# wrapper_function()

# def benchmark(func):
#     import time
#
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'время выполнения - {end - start} секунд')
#     return wrapper()
#
# @benchmark
# def fetch_webpage():
#     import requests
#     webpage = requests.get('https://google.com')
#
# fetch_webpage()
#
# def benchmark(iters):
#     def actual_decorator(func):
#         import time
#
#         def wrapper(*args, **kwargs):
#             total = 0
#             for i in range(iters):
#                 start = time.time()
#                 return_value = func(*args, **kwargs)
#                 end = time.time()
#                 total = total + (end - start)
#             print(f'среднее время выполнения {total/iters} секунд')
#             return return_value
#         return wrapper
#     return actual_decorator
#
# @benchmark(iters=2)
# def fetch_webpage(url):
#     import requests
#     webpage = requests.get(url)
#     return webpage.text
#
# webpage = fetch_webpage('https://google.com')
# print(webpage)

# def makebold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#
#     return wrapped
#
#
# def makeitalic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#
#     return wrapped
#
#
# @makebold
# @makeitalic
# def hello():
#     return "hello habr"
#
#
# print(hello())


# def send_email(settings=None):
#     time.sleep(random.randint(1, 3))
#
#
# send_email(settings={'smtp': 'smtp.google.com'})
# send_email(settings={'smtp': 'smtp.outlook.live.com'})

# def send_email(settings=None):
#     time.sleep(random.randint(1, 3))
#
# start = time.time()
# send_email(settings={'smtp': 'smtp.google.com'})
# end = time.time()
# print(f'Elapsed: {end - start}s')
#
# start = time.time()
# send_email(settings={'smtp': 'smtp.outlook.live.com'})
# end = time.time()
# print(f'Elapsed: {end - start}s')

# def send_email(settings=None):
#     start = time.time()
#
#     time.sleep(random.randrange(1, 3))
#
#     end = time.time()
#     print(f'Elapsed  with {settings}: {end - start}s')
#
# send_email(settings={'smtp': 'smtp.google.com'})
# send_email(settings={'smtp': 'smtp.outlook.live.com'})

def dump_database(storage: object = None) -> object:
    start = time.time()

    time.sleep(random.randrange(0, 1))

    end = time.time()
    print(f'Elapsed with {storage}: {end - start}s')

dump_database(storage='s3')
dump_database(storage='gdrive')