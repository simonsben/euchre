from random import randint

def random_number(max):
    return randint(0, max)

def get_player(player):
    while player > 3:
        player -= 4

    return player

def isLegal(trump, card):
    if card.suit == trump:
        return True
    elif card.rank == 2:
        if   card.suit == 'H' and trump == 'D': return True
        elif card.suit == 'D' and trump == 'H': return True
        elif card.suit == 'S' and trump == 'C': return True
        elif card.suit == 'C' and trump == 'S': return True

    return False


suits = [
    'H',
    'D',
    'S',
    'C'
]

suit_lookup = {
    'H': 'Hearts',
    'D': 'Diamonds',
    'S': 'Spades',
    'C': 'Clubs'
}

ranks = [
    0,
    1,
    2,
    3,
    4,
    5
]

rank_lookup = {
    0: '9',
    1: '10',
    2: 'Jack',
    3: 'Queen',
    4: 'King',
    5: 'Ace'
}

sample_players = [
    'aa',
    'bb',
    'cc',
    'dd'
]
