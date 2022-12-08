import random

# Вариант для игрока с ботом (без ИИ).
# Нужно доработать еще немного последний ход бота
print('''Перед игроками куча из 2021 конфеты. Игра идет до тех пор, пока не останется конфет в куче. 
За один ход можно взять не более 28 конфет. Очередность определяется случайным образом.
Победителем является игрок, сделавший последний ход.
''')
count_of_candies = 2021
first_move = random.random()
moves = ['Ход игрока номер 1', 'Ход бота']
if first_move > 0.5:
    print('Первый ход у игрока номер 1')
else:
    moves.sort()
    print('Первый ход бота')
player = 0
while count_of_candies > 0:
    print(moves[player])
    if moves[player] == 'Ход бота':
        step_count = random.randint(1, 28)
        print(f'Бот взял {step_count} конфет')
    else:
        step_count = int(input('Сколько конфет хотите взять: '))
    if 0 < step_count < 29 and not(step_count > count_of_candies):
        count_of_candies -= step_count
        if count_of_candies <= 0:
            print(f'Конфет не осталось!!!')
            if len(moves[player]) == 8:
                print('Бот выиграл!')
            else:
                print(f'Победил игрок {moves[player][11:]}')
        else:
            print(f'Осталось {count_of_candies} конфет')
            player = (player + 1) % 2
    else:
        print('Не правильный ход!')
