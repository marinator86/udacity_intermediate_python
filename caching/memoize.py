import functools

def memoize(function):
    function._cache = {}
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if(key in function._cache):
            return function._cache.get(key)
        result = function(*args, **kwargs)
        function._cache[key] = result
        return result
    return wrapper