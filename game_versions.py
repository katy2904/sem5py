# sweets = 25
# K = 5
# p1, p2 = 'qq', 'ww'

#игра с человеком
def human_vs_human(sweets, K, p1, p2):
    while sweets > 0:
        first = int(input(f'Игрок {p1} возьмите конфеты от 1 до {K}: '))
        print(f'Осталось {sweets - first} конфет')
        if sweets - first <= 0:
            win = p1
            break
        else:
            second = int(input(f'Игрок {p2} возьмите конфеты от 1 до {K}: '))
            sweets -= (first + second)
            print(f'Осталось {sweets} конфет')
            if sweets <= 0:
                win = p2
    return win

# print(human_vs_human(sweets, K, p1, p2))