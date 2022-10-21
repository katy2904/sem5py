# Создайте программу для игры с конфетами человек против человека.
# Добавьте игру против бота
# Подумайте как наделить бота ""интеллектом""



import draw
import game_versions

print('Давай поиграем! Смысл игры простой:')
print('На столе лежит N конфет. За 1 ход можно взять не более K конфет. Все конфеты достанутся '
      'тому, кто сделает последний ход')

print('Как будем играть? 0 - против человека, 1 - против бота.')
while True:
      version = int(input())
      if version == 0 or version == 1:
            break
      else:
            print('Такого варианта нет, увы... Есть только 0 и 1, выбираем из них')


player1 = input('Введите имя первого игрока: ')
if version == 0:
      player2 = input('Введите имя второго игрока: ')
else:
      player2 = 'SMART-бот'


N = int(input('Сколько конфет положим на стол?: '))
K = int(input('Какое максимальное количество конфет можно взять за 1 ход: '))

print('А теперь жеребьевка! Бросаем кубики!')

p1 = draw.player_draw(player1, player2)
print(f'Первый ход делает {p1}')

if p1 == player1:
      p2 = player2
else:
      p2 = player1

if version == 0:
      win = game_versions.human_vs_human(N, K, p1, p2)
elif version == 1 and p1 == player1:
      win = game_versions.human_vs_smartbot(N, K, p1, p2)
else:
      win = game_versions.smartbot_vs_human(N, K, p1, p2)

print(f'Поздравляю с победой, {win}!')