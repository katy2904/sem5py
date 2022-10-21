# sweets = 25
# K = 3
# p1, p2 = 'sb', 'ww'

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

#print(human_vs_human(sweets, K, p1, p2))

#игра с умным ботом
def smart_bot_step(sweets, K):
    if sweets > K:
        step = sweets % (K + 1)
    else:
        step = K
    return step


def human_vs_smartbot(sweets, K, p1, p2):
    while sweets > 0:
        first = int(input(f'Игрок {p1} возьмите конфеты от 1 до {K}: '))
        sweets -= first
        print(f'Осталось {sweets} конфет')
        if sweets <= 0:
            win = p1
            break
        else:
            second = smart_bot_step(sweets, K)
            print(f'Бот берет {second} конфет')
            sweets -= second
            print(f'Осталось {sweets} конфет')
            if sweets <= 0:
                win = p2
    return win

def smartbot_vs_human(sweets, K, p1, p2):
    while sweets > 0:
        first = smart_bot_step(sweets, K)
        print(f'Бот берет {first} конфет')
        sweets -= first
        print(f'Осталось {sweets} конфет')
        if sweets <= 0:
            win = p1
            break
        else:
            second = int(input(f'Игрок {p1} возьмите конфеты от 1 до {K}: '))
            sweets -= second
            print(f'Осталось {sweets} конфет')
            if sweets <= 0:
                win = p2
    return win

#print(win)