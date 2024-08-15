def get_multiplied_digits(number):
    str_number = str(number)
    if str_number == '0':
        return 1
    if len(str_number) == 1:
        return number
    first = int(str_number[0])
    next_number = int(str_number[1:])
    return first * get_multiplied_digits(next_number)


result = get_multiplied_digits(40203)
print(result)