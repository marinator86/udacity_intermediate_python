"""Generate an infinite stream of successively larger random lists."""
import functools
import itertools
import helper


# The generic approach to decorate functions using variadic pos/keyword arguments. Sure, every function can be expressed
# by *args, **kwargs, but I'm "missing" types a bit because I'm used to them. Though, decorators indeed decouple and
# modularize functionality, which then can be plugged together.
# From OOP, I'm used to couple objects to each other using relations (state). This is indeed very different. No more
# stateful objects, but stateful function (-objects) instead (e.g. using _cache).

def do_nothing(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print("nop")
        return function(*args, **kwargs)
    return wrapper

@do_nothing
def print_args(times = 1):
    def print_args2(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                print(args, kwargs)
            return function(*args, **kwargs)
        return wrapper
    return print_args2

def generate_cases_another_alternative():
    return map(helper.random_list, itertools.count())

def generate_cases_alternative():
    return (helper.random_list(size) for size in itertools.count())

@print_args(times=2)
def generate_cases():
    i = 1
    while True:
        yield helper.random_list(i)
        i += 1

@print_args(times=3)
def doFuzzing(i):
    for case in generate_cases():
        if len(case) > i:
            break
        print(case)


if __name__ == '__main__':
    doFuzzing(10)