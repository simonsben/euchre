from random import randint

def random_number(max):
    return randint(0, max)

def get_player(player):
    while player > 3:
        player -= 4

    return player


suit = [
    'H',
    'D',
    'S',
    'C'
]

rank = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12
]
