print('x y z Значение функции')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(x or y or z) == (not x) and (not y) and (not z):
                print(x, y, z, '\t Истина')
            else:
                print(x, y, z, '\t  Ложь')
