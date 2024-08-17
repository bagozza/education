from math import inf


def divide(first, second):
    if second == 0:
        print(inf)

    if second != 0:
        a = first / second
        print(a)

    return first, second



