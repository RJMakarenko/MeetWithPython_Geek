first_point = [int(x) for x in input('Введите координаты первой точки через пробел: ').split()]
second_point = [int(x) for x in input('Введите координаты второй точки через пробел: ').split()]
distance = ((first_point[0] - second_point[0]) ** 2 + (first_point[1] - second_point[1]) ** 2) ** 0.5
print(f'Расстояние между точками {first_point} и {second_point} = {str(distance)[:4]}')

