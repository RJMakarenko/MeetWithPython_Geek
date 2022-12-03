lst = [x for x in range(1, 20)]
print(f'Исходный список: {lst}')
sum_of_elements = sum(lst[i] for i in range(1, len(lst), 2))
print(f'Сумма значений элементов на нечетных индексах: {sum_of_elements}')
