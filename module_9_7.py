def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res % 2 == 0:
            print('Составное')
        elif res <= 1:
            print('Составное')
        else:
            print('Простое')

        return res

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
