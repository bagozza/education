from random import randint

n = randint(3, 20)
result = ""
for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            result += f'{i}{j}'
print(f'{n} - {result}')
