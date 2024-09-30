def apply_all_func(int_list, *functions):
    result = {}
    for fun in functions:
        result[fun.__name__] = fun(int_list)
    print(result)


apply_all_func([6, 20, 15, 9], max, min)
apply_all_func([6, 20, 15, 9], len, sum, sorted)

