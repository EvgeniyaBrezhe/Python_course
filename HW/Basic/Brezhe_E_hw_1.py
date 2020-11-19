import functools
import time

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

foo(5)
foo(6)
foo(5)
foo(6)
foo(7)
foo(8)
foo(5)
foo(6)


