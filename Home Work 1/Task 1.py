day_of_week = int(input('Введите номер дня недели: '))
if day_of_week in [6, 7]:
    print(f'Да. {day_of_week} день недели - это выходной')
elif day_of_week in [1, 2, 3, 4, 5]:
    print(f'Нет. {day_of_week} день недели - это будний день')
else:
    print('В неделе всего 7 дней! \N{winking face}')
