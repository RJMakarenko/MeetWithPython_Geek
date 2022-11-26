import random

input_list = [x for x in range(1, 20)]
print(f'Исходный список: {input_list}')
random.shuffle(input_list)
print(f'Случайное перемешивание: {input_list}')
