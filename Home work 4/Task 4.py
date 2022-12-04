import random

k = int(input('Введите старшую степень многочлена: '))
coefficients = [random.randint(0, 100) for i in range(k)]
print(f'Случайные коэффициенты: {coefficients}')
result_string = ''
for i in range(k, -1, -1):
    if coefficients[i - 1] != 0:
        if i == 1:
            result_string += f'{coefficients[i - 1]}*x + '
        elif i == 0:
            result_string += f'{coefficients[i - 1]}'
        else:
            result_string += f'{coefficients[i - 1]}*(x**{i}) + '
    else:
        continue
result_string += ' = 0'
with open('file 2.txt', 'w') as result_file:
    print(result_string, file=result_file)
print('Результат смотри в файле "task 4.txt"')
