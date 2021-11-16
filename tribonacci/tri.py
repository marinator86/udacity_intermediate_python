
def generate_tribonacci_numbers():
    a, b, c = 0, 0, 1
    # Yield an infinite stream of Tribonacci numbers! The next value of the sequence will be c + b + a.
    while True:
        yield a
        a, b, c = b, c, a + b + c


def is_tribonacci(num):
    """Return whether `num` is a Tribonacci number."""
    for trib in generate_tribonacci_numbers():
        if num == trib:
            print(f"{num} is a tribonacci")
            return True
        if num < trib:
            print(f"{num} is not a tribonacci")
            return False

if __name__ == '__main__':

    list(map(is_tribonacci, [2698569577, 4, 36, 72]))