from random import randrange

input_list = [x for x in range(1, 20)]
print(f'Исходный список: {input_list}')
random_elements = set()
for i in range(len(input_list)):
    take = randrange(0, len(input_list))
    if input_list[take] not in random_elements:
        random_elements.add(input_list[take])
        past = randrange(0, len(input_list))
        el = input_list[take]
        input_list.remove(el)
        input_list.insert(past, el)
print(f'Случайное перемешивание: {input_list}')
