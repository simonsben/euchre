from utilities import random_number, get_player, sample_players
from deck import deck
from player import player

# Players are indexed from 0 to 3, going clockwise

class game:
    def __init__(self): # Initialize a new game
        dealer_id = random_number(3)    # Choose random first dealer
        self.dealer = dealer_id     # Assign the dealer ID
        self.turn = get_player(dealer_id + 1)   # Assign who's turn it is

        self.gen_players()  # Generate players
        self.deck = deck()  # Generate the deck
        self.kitty = []

        self.deal_cards()

    def deal_cards(self):
        for i, card in enumerate(self.deck.cards):
            if i  >= 20:
                self.kitty.append(card)
            else:
                self.players[get_player(i)].add_card(card)

    def gen_players(self):
        self.players = []
        for i, name in enumerate(sample_players):
            self.players.append(player(i, name))

    def __str__(self):
        output = ''
        for player in self.players:
            output += player.__str__() + '\n'

        return output
