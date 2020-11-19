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

# def dump_database(storage: object = None) -> object:
#     start = time.time()
#
#     time.sleep(random.randrange(0, 1))
#
#     end = time.time()
#     print(f'Elapsed with {storage}: {end - start}s')
#
# dump_database(storage='s3')
# dump_database(storage='gdrive')

# def some_other_func(*args):
#     start = time.time()
#
#     lst = [i for i in range(10**6)]
#
#     print(f'Elapsed {args}: {time.time() - start}s')
#
# some_other_func()

# def dump_database(storage=None):
#     time.sleep(random.randrange(0, 1))
#
# def send_email(settings=None):
#     time.sleep(random.randint(1, 3))
#
# def profile(f):
#     start = time.time()
#
#     f()
#
#     print(f'Elapsed: {time.time() - start}s')
#
# profile(dump_database)
# profile(send_email)

# def say_hello():
#     def internal():
#         print('Hello')
#     return internal
#
# f = say_hello()
# print(type(f))
# f()

# def say_hello():
#     def internal(msg):
#         print('Hello', msg)
#     return internal
#
# f1 = say_hello()
# f1('John')
#
# f1 = say_hello()
# f1('Bill')

# def say_hello(greeting='Hello'):
#     def internal(msg):
#         print(greeting, msg)
#     return internal
#
# f1 = say_hello()
# f1('John')
#
# f1 = say_hello('Hi')
# f1('Bill')
#
# print("__________")
#
# def say_hello(greeting='Hello'):
#     def internal(*args):
#         print(greeting, *args)
#     return internal
#
# f1 = say_hello()
# f1('John', 42, [1, 2, 3], True)

# def profile(f):
#     def deco(*args):
#         start = time.time()
#         result = f(*args)
#         print(f'Elapsed time for function {f.__name__}: {time.time() - start}ms')
#         return result
#
#     return deco
#
# @profile
# def foo6():
#     time.sleep(random.randint(1, 2))
#     return 42
#
# print(foo6())

# def profile(msg):
#     def internal(f):
#         # @functools.wraps(f)
#         def deco(*args):
#             start = time.time()
#             result = f(*args)
#             print(msg, f'{f.__name__}: {time.time() - start}ms')
#             return result
#         return deco
#     return internal
#
# @profile('Elapsed time') # -> profile_ = profile('Time spent')
#                        # -> foo5 = profile_(foo5)
# def foo8():
#     """Help for foo7"""
#     time.sleep(random.randint(1, 2))
#     return 42
#
# help(foo8)
# print("RESULT: ", foo8())

# def repeate(max_repeat=10):
#     def internal(f):
#         @functools.wraps(f)
#         def repeater(*args, **kwargs):
#             while repeater._num_repeats <= max_repeat:
#                 try:
#                     f(*args, **kwargs)
#                 except Exception as ex:
#                     if repeater._num_repeats == max_repeat:
#                         raise
#                     else:
#                         print(
#                             f'Failed after {repeater._num_repeats + 1} times, trying again after {2 ** repeater._num_repeats} sec...')
#                         sleep(2 ** repeater._num_repeats)
#                         repeater._num_repeats += 1
#
#         repeater._num_repeats = 0
#         return repeater
#
#     return internal
#
#
# @repeate(max_repeat=4)
# # @repeate()
# # @repeate # note the difference
# def connect_to_server(*args):
#     print('Trying to connect: ', *args)
#     raise RuntimeError('Failed to connect')
#
#
# connect_to_server('google.com')

# def profile(msg="Elapsed time for function"):
#     def internal(f):
#         @functools.wraps(f)
#         def deco(*args):
#             start = time.time()
#             result = f(*args)
#             print(msg, f'{f.__name__}: {time.time() - start}ms')
#             return result
#
#         return deco
#
#     return internal
#
# def cache(max_size=0):
#     def one_more_function(f):
#
#         @functools.wraps(f)
#         def deco(*args):
#             if len(deco._cache) <= max_size:
#                 if args in deco._cache:
#                     return deco._cache[args]
#
#                 result = f(*args)
#
#                 deco._cache[args] = result
#                 print(type(deco._cache))
#                 print(len(deco._cache))
#             else:
#                 print("I can't do nothing more")
#
#             return result
#
#
#         deco._cache = {}
#
#         return deco
#     return one_more_function
#
# @profile()
# @cache(max_size=1)
# def foo(n):
#     time.sleep(n)
#
# foo(5)
# foo(6)
# foo(5)
# foo(6)

# def profile(msg="Time spent on this:"):
#     def internal(f):
#         @functools.wraps(f)
#         def deco(*args):
#             start = time.time()
#             result = f(*args)
#             print(msg, f'{f.__name__}: {time.time() - start}ms')
#             return result
#
#         return deco
#
#     return internal
#
# def cache(max_size=2):
#     def cache_internal(f):
#         @functools.wraps(f)
#         def deco(*args):
#
#             if args in deco._cache:
#                 return deco._cache[args]
#
#             result = f(*args)
#
#             # if len(deco._cache) > max_size:
#             #     deco._cache.pop(list(deco._cache.keys())[0])
#
#             deco._cache[args] = result
#
#             return result
#
#         deco._cache = {}
#
#         return deco
#     return cache_internal
#
# @profile()
# @cache()
# def foo(n):
#     time.sleep(n)
#
# foo(5)
# foo(5)
# foo(6)
# foo(6)
# foo(7)
# foo(7)
# foo(8)
# foo(8)
# foo(9)
# foo(9)

#
# my_dict = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e"}
# print(my_dict, type(my_dict))
#
# a = list(my_dict.keys())
# print(a[0], type(a))
#
# my_dict.pop(a[0])
# print(my_dict)

def profile(msg="Time spent"):
    def internal(f):
        @functools.wraps(f)
        def deco(*args):
            start = time.time()
            result = f(*args)
            print(msg, f'{f.__name__}: {time.time() - start}ms')
            return result
        return deco
    return internal

def cache(max_limit=2):
    def cache_additional(f):
        @functools.wraps(f)
        def deco(*args):
            if args in deco._cache:
                return deco._cache[args]

            result = f(*args)

            if len(deco._cache) > max_limit:
                deco._cache.pop(list(deco._cache.keys())[0])

            deco._cache[args] = result

            return result

        deco._cache = {}

        return deco
    return cache_additional

@profile()
@cache(max_limit=2)
def foo(n):
    time.sleep(n)

foo(1)
foo(2)
foo(1)
foo(2)
foo(5)
foo(6)
foo(5)
foo(6)
foo(1)
