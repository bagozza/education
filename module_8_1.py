def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError as exc:
        print(str(a) + str(b))
    finally:
        print('Готово!')


(add_everything_up(123.456, 'строка'))
(add_everything_up('яблоко', 4215))
(add_everything_up(123.456, 7))
