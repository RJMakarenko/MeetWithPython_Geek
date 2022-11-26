n = int(input('Введите число: '))
result = sum(map(lambda x: (1 + 1 / x) ** x, [x for x in range(1, n + 1)]))
print(str(result)[:4])
