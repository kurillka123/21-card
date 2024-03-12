from random import shuffle
from os import system


'''
Карты:
    имя
    цена
    масть

Колода: всего карт = цены * масти
    в 1 масти: 6, 7, 8, 9, 10, валет, дама, король, туз

Игроки - от 2 штук

Колода перемешивается

Кажому игроку выдается по 2 карты из колоды

Игрок видит только свои карты

Задача - цены всех карт игрока = 21

Ход игрока:
    оставить свои карты и больше не набирать
    или взять еще карту (сколько угодно раз)

Все игроки должны закончить ход

Если у игрока сумма цен всех карт > 21, он проиграл
Если у всех игроков проигрыш, то это ничья

Выигрывает тот, у кого больше очков и тот, кто не проиграл
'''


def get_deck() -> list[dict]:
    suits = [chr(4) , chr(3) , chr(6), chr(5)]
    names = ['6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    deck = []  # создаем колоду

    for suit in suits:
        for name in names:
            if name in ('валет', 'дама', 'король'):
                value = 10
            elif name == 'туз':
                value = 11
            else:
                value = int(name)
            card = {
                'имя': name,
                'цена': value,
                'масть': suit,
            }
            deck.append(card)
    return deck

def get_players():
    player_1 = {
        'человек': True,
        'имя': 'вася',
        'карты': [],
        'счет': 10
    }
    player_2 = {
        'человек': True,
        'имя': 'ася',
        'карты': [],
        'счет': 10
    }
    return [player_1, player_2]

def deal_cards(num: int) -> None:
    for player in players:
        for _ in range(num):
            player['карты'].append(deck.pop(-1))

def show_cards() -> None:
    for card in player['карты']:
        print(card['имя'], card['масть'])

deck = get_deck()
shuffle(deck)
players = get_players()
max_card_per_turn = len(deck) // len(players)
deal_cards(2)

def get_total_cards_values(player: dict) -> int:
    ''' возвращает сумму цен карт игрока'''
    total = 0
    for card in player['карты']:
        total += card['цена']
    return total

for player in players:
    while True:
        system('cls')
        print('ход игрока:', player['имя'])
        print('-' * 20)
        show_cards()
        print('сумма очков:', get_total_cards_values(player))
        print('-' * 20)
        print('/ бубны: ', chr(4), ', черви: ', chr(3), ', пики: ', chr(6), ', крести: ', chr(5), '/')
        print('-' * 20)
        player_option = input('взять карту? y/n:')
        if player_option == 'y':
            if len(player['карты']) < max_card_per_turn:
                player['карты'].append(deck.pop(-1))
            else:
                ('невозможно взять еще карту!')
                break
        else:
            break

total_player = []
for player in players:
    total_player.append(get_total_cards_values(player))

candidates = []
for value in total_player:
    if value < 21:
        candidates.append(value)

for value in total_player:
    index = total_player.index(max(total_player))
    player = players[index]
    if value > 21:
        print(player['имя'], value, '- перебор')
    elif total_player == 21:
        print(player['имя'], total_player, '- победил')
    else:
        pass
    