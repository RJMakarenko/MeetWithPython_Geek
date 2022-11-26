n = int(input('Введите число: '))
input_list = [x for x in range(-n, n + 1)]
print(f'Результат построения списка: {input_list}')
indexes = [int(x) for x in input('Введите номера необходимых индексов черех пробел: ').split()]
result = 1
for ind in indexes:
    result *= input_list[ind]
print(f'Произведение значений списка на указанных индексах: {result}')
