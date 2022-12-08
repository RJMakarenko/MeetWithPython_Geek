import random

# Вариант для двух игроков
print('''Перед игроками куча из 2021 конфеты. Игра идет до тех пор, пока не останется конфет в куче. 
За один ход можно взять не более 28 конфет. Очередность определяется случайным образом.
Победителем является игрок, сделавший последний ход.
''')
count_of_candies = 2021
first_move = random.random()
moves = ['Ход игрока номер 1', 'Ход игрока номер 2']
if first_move > 0.5:
    print('Первый ход у игрока номер 1')
else:
    moves.sort(reverse=True)
    print('Первый ход у игрока номер 2')
player = 0
while count_of_candies > 0:
    print(moves[player])
    step_count = int(input('Сколько конфет хотите взять: '))
    if 0 < step_count < 29:
        count_of_candies -= step_count
        print(f'Осталось {count_of_candies} конфет')
        if count_of_candies == 0:
            print(f'Победил игрок {moves[player][11:]}')
        player = (player + 1) % 2
    else:
        print('Не правильный ход!')
