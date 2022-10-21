


def human_vs_human(sweets, K, p1, p2):
    while sweets > 0:
        if sweets <= K:
            win = p1
            break
        else:
            while True:
                first = int(input(f'Игрок {p1} возьмите конфеты от 1 до {K}: '))
                if first not in range(1, K + 1):
                    print('Неверное значение, попробуй ещё раз: ')
                else:
                    break
            sweets -= first
            print(f'Осталось {sweets} конфет')
            if sweets <= K:
                win = p2
                break
            else:
                while True:
                    second = int(input(f'Игрок {p2} возьмите конфеты от 1 до {K}: '))
                    if second not in range(1, K + 1):
                        print('Неверное значение, попробуй ещё раз: ')
                    else:
                        break
                sweets -= second
                print(f'Осталось {sweets} конфет')
    return win



def smart_bot_step(sweets, K):
    return sweets % (K + 1)


def human_vs_smartbot(sweets, K, p1, p2):
    while sweets > 0:
        if sweets <= K:
            win = p1
            break
        else:
            while True:
                first = int(input(f'Игрок {p1} возьмите конфеты от 1 до {K}: '))
                if first not in range(1, K + 1):
                    print('Неверное значение, попробуй ещё раз: ')
                else:
                    break
            sweets -= first
            print(f'Осталось {sweets} конфет')
            if sweets <= K:
                win = p2
                break
            else:
                second = smart_bot_step(sweets, K)
                print(f'Бот берет {second} конфет')
                sweets -= second
                print(f'Осталось {sweets} конфет')

    return win

def smartbot_vs_human(sweets, K, p1, p2):
    while sweets > 0:
        if sweets <= K:
            win = p1
            break
        else:
            first = smart_bot_step(sweets, K)
            print(f'Бот берет {first} конфет')
            sweets -= first
            print(f'Осталось {sweets} конфет')
            if sweets <= K:
                win = p2
                break
            else:
                while True:
                    second = int(input(f'Игрок {p2} возьмите конфеты от 1 до {K}: '))
                    if second not in range(1, K + 1):
                        print('Неверное значение, попробуй ещё раз: ')
                    else:
                        break
                sweets -= second
                print(f'Осталось {sweets} конфет')
    return win

