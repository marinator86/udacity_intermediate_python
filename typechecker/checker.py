import functools
import helper

def check_types(severity=1):
    if severity == 0:
        return lambda function: function

    def msg(msg):
        if severity == 1:
            print(msg)
        else:
            raise TypeError(msg)

    def checker(function):
        annotations = function.__annotations__

        if not annotations:
            return function

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            bindings = dict(helper.bind_args(function, *args, **kwargs))
            for param, p_val in bindings.items():
                if type(p_val) != annotations[param]:
                    msg(f"{function.__name__} param {param} has type {annotations[param]} but was called with {type(p_val)}")
            ret = function(*args, **kwargs)
            if annotations['return']:
                if type(ret) != annotations['return']:
                    msg(f"{function.__name__} has return type {annotations['return']} but returned {type(ret)}")
            return ret
        return wrapper
    return checker

@check_types(severity=2)
def wrong_return() -> bool:
    return "wrong_string"

@check_types(severity=2)
def equals(a: int, b: int) -> bool:
    return a == b

@check_types(severity=2)
def just_pass():
    pass

if __name__ == '__main__':
    print(equals(1, 1))
    try:
        equals(2, "2")
    except TypeError as e:
        print(e)
    try:
        wrong_return()
    except TypeError as e:
        print(e)
    print(just_pass())