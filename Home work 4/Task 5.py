with open('file 1.txt', 'r') as file_1:
    with open('file 2.txt', 'r') as file_2:
        string1 = file_1.readline()
        string2 = file_2.readline()
print(f'Первый многочлен: {string1}', end='')
print(f'Второй многочлен: {string2}', end='')
# Избавляемся от знаков сложения и лишних пробелов
list_1 = string1.split(' + ')
# Избавимся от " = 0" в последнем элементе списка
list_1[-1] = list_1[-1][:-5]
list_2 = string2.split(' + ')
# Избавимся от " = 0" в последнем элементе списка
list_2[-1] = list_2[-1][:-5]
# Создадим два словаря (для первого и второго многочлена). В них будем хранить числа и коэффициенты степеней
first_dictionary = {}
second_dictionary = {}
for item in list_1:
    item_list = item.split('*')
    # Если длина элемента более 1 - значит это степень старше 0
    if len(item_list) > 1:
        # Если в элементе есть скобка - значит это степень больше 1
        if ')' in item:
            # Избавимся от скобки
            first_dictionary[item_list[-1][:-1]] = int(item_list[0])
        else:
            # Если скобки нет - это 1 степень
            first_dictionary['1'] = int(item_list[0])
    # Если длина элемента 1 - значит это 0 степень
    else:
        first_dictionary['0'] = int(item_list[0])
for item in list_2:
    item_list = item.split('*')
    if len(item_list) > 1:
        if ')' in item:
            second_dictionary[item_list[-1][:-1]] = int(item_list[0])
        else:
            second_dictionary['1'] = int(item_list[0])
    else:
        second_dictionary['0'] = int(item_list[0])
# Создадим словарь для сумм коэффициентов многочлена (складываются эелементы с одинаковой степенью)
# Если степень присутствует только в одном из многочленов - просто переписываем её
result_dictionary = {}
# Определим какой многочлен больше (найдем старшую возможную степень)
max_len = len(first_dictionary) if len(first_dictionary) > len(second_dictionary) else len(second_dictionary)
# В цикле пройдем от старшей степени до 0
for i in range(max_len - 1, -1, -1):
    # Если такая степень отсутствует в словаре - вместо неё запишем 0
    first_number = 0 if first_dictionary.get(str(i)) is None else first_dictionary.get(str(i))
    second_number = 0 if second_dictionary.get(str(i)) is None else second_dictionary.get(str(i))
    # В итоговой словарь запишем сумму коэффициентов
    result_dictionary[str(i)] = first_number + second_number
# Соберем результирующую строку - результат сложения многочленов
result_string = ''
for key, value in result_dictionary.items():
    if key == '1':
        result_string += f'{value}*x + '
    elif key == '0':
        result_string += f'{value}'
    else:
        result_string += f'{value}*(x**{key}) + '
result_string += ' = 0'
print(f'Результат сложения: \n{result_string}')
