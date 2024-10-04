# import sys
# from itertools import repeat
#
#
# ex_iterator = repeat('4', 100_000)
# print(ex_iterator)
# print(f'Размер итератора - {sys.getsizeof(ex_iterator)}')
#
# ex_str = '4' * 100_000
# print(f'Размер списка - {sys.getsizeof(ex_str)}')
# def fibonacci(n):
#     res = []
#     a, b = 0, 1
#     for _ in range(n):
#         res.append(a)
#         a, b = b, a + b
#     return res
#
#
# for value in fibonacci(n=10):
#     print(value)
#
# class Fibonacci:
#     def __init__(self, n):
#         self.i = 0
#         self.a = 0
#         self.b = 1
#         self.n = n
#
#     def __iter__(self):
#         self.i = 0
#         self.a = 0
#         self.b = 1
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > 1:
#             if self.i > self.n:
#                 raise StopIteration()
#             self.a, self.b = self.b, self.a + self.b
#         return self.a
#
#
# fib_iterator = Fibonacci(20)
# print(fib_itertor)
#
# for value in fib_itertor:
#     print(value)

class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step > 0 and self.pointer > self.stop:
            raise StopIteration
        if self.step < 0 and self.pointer < self.stop:
            raise StopIteration
        res = self.pointer
        self.pointer += self.step
        return res


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
