from collections import Counter

lst_1 = [1, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 4]
# создадим словарь, содержащий числа в качестве ключей, и количество чисел в качестве значений
result_dictionary = Counter(lst_1)
result = []
# получим ключи и значения, если значение = 1 - значит это число подходит
for key, value in result_dictionary.items():
    if value == 1:
        result.append(key)
print(result)
