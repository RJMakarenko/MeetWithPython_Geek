from math import factorial

n = int(input('Введите число: '))
result = []
for i in range(1, n + 1):
    result.append(factorial(i))
print(f'Набор произведение чисел от 1 до {n}: {result}')
