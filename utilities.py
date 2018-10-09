from random import randint

def random_number(max):
    return randint(0, max)

def get_player(player):
    return player % 4

def get_input(prompt, options):
    answer = input(prompt)
    while answer not in options:
        answer = input('This it not a valid option, choose again. ' + str(options))

    return answer

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

suit_pair = {
    'H': 'D',
    'D': 'H',
    'S': 'C',
    'C': 'S'
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

def ask_order_up(prompt, players):
    prompt_options = ['y', 'n']

    for player in players:
        print(player.name, ' is up')
        print(player)

        answer = get_input(prompt, prompt_options)
        if answer != 'n':
            return player.id

    return -1

def ask_other_suits(prompt, prompt_options, players):
    pass_charater = 'p'
    prompt_options.append(pass_charater)

    for player in players:
        print(player.name, ' is up')
        print(player)

        answer = get_input(prompt, prompt_options)
        if answer != pass_charater:
            return answer

    return pass_charater
