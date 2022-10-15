import random

def player_draw(pl_1, pl_2):
    pl_1_1, pl_1_2, pl_2_1, pl_2_2 = 0, 0, 0, 0
    while (pl_1_1 + pl_1_2) == (pl_2_1 + pl_2_2):
        print(f'{pl_1} бросает:')
        pl_1_1, pl_1_2 = random.randint(1, 6), random.randint(1, 6)
        print(f'выпало {pl_1_1} и {pl_1_2}. Сумма {pl_1_1 + pl_1_2}')
        print()

        print(f'{pl_2} бросает:')
        pl_2_1, pl_2_2 = random.randint(1, 6), random.randint(1, 6)
        print(f'выпало {pl_2_1} и {pl_2_2}. Сумма {pl_2_1 + pl_2_2}')
        print()

        if (pl_1_1 + pl_1_2) == (pl_2_1 + pl_2_2):
            print('Ничья! Кидаем еще раз!')

    if (pl_1_1 + pl_1_2) > (pl_2_1 + pl_2_2):
        return print(f'Первый ход делает {pl_1}')
    elif (pl_1_1 + pl_1_2) < (pl_2_1 + pl_2_2):
        return print(f'Первый ход делает {pl_2}')