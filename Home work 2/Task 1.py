number = float(input('Введите число: '))
print(sum(map(int, [x for x in str(number) if x.isnumeric()])))


