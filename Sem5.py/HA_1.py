# 1. Создайте программу для игры с конфетами человек против человека.
# *' Условие игры: На столе лежит 117 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота

#variant players

text = print('\nУсловие игры: На столе лежит 117 конфета.Играют два игрока делая ход друг после друга. \nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. \nВсе конфеты оппонента достаются сделавшему последний ход.\n')


from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: \n"))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: \n"))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.\n")

player1 = input("Введите имя первого игрока: \n")
player2 = input("Введите имя второго игрока: \n")
value = int(input("Введите количество конфет на столе: \n"))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}\n")
else:
    print(f"Первый ходит {player2}\n")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

#player_vs_bot

from random import randint
message = ['Руки-загребуки', 'Главное чтобы не слиплось', 'Бери больше шоколадных', 'Чем больше - тем лучше']
def player_vs_bot():
    candies = 117
    max_take = 28
    count = 0
    player_1 = input('\nКак зовут тебя? ')
    print(f'Привет {player_1}!')
    player_2 = 'Bot'
    players = [player_1, player_2]

    print(f'{player_2} приветствует игрока {player_1}\n')
    print('Кто же будет первым?! Да решит же всё жребий!\n')

    winner = randint(-1, 0)

    print(f'{players[winner + 1]} удачлив, ходи первым!')
    import random
    while candies > 0:
        winner = winner + 1

        if players[winner % 2] == 'Bot':
            if candies < 29:
                round = candies  # забирает оставшиеся конфеты
            else:
                delenie = candies // 28
                round = candies - ((delenie * max_take) + 1)
                if round == -1:
                    round = max_take - 1
                if round == 0:
                    round = max_take
            while round > 28 or round < 1:
                round = randint(1, 28)
            print(round)
            if candies > 0:
                candies = candies - round
        else:
            round = int(input(f'{random.choice(message)}  {players[winner % 2]}! \n '))
            if round > candies or round > max_take:
                print(f'Кому-то не хватает сладкого? Можно взять {max_take}, давай сначала: ')
                continue
            else:
                candies = candies - round
        if candies > 0:
                print(f'Осталось ещё {candies} конфет, игра продолжается! \n')
    print(f'На кону осталось {candies} \nПобедил {players[winner % 2]}')

player_vs_bot()