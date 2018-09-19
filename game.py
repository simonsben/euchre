from utilities import random_number, get_player, sample_players
from deck import deck
from player import player
from team import team

# Players are indexed from 0 to 3, going clockwise

class game:
    def __init__(self): # Initialize a new game
        dealer_id = random_number(3)    # Choose random first dealer
        self.dealer = dealer_id     # Assign the dealer ID
        self.turn = get_player(dealer_id + 1)   # Assign who's turn it is

        self.gen_players()  # Generate players
        self.deck = deck()  # Generate the deck

        self.kitty = []     # Initialize the kitty
        self.hands = []     # Initialize hands
        self.trump = None   # Initialize trump

        self.make_teams()   # Split players into teams
        self.deal_cards()   # Divide cards between players

    # Divide cards between players
    def deal_cards(self):
        for i, card in enumerate(self.deck.cards):
            if i  >= 20:
                self.kitty.append(card)
            else:
                self.players[get_player(i)].add_card(card)

    # Generate players
    def gen_players(self):
        self.players = []
        for i, name in enumerate(sample_players):
            self.players.append(player(i, name))

    # Make teams
    def make_teams(self):
        self.teams = []
        players = self.players
        self.teams.append(team(players[0], players[2]))
        self.teams.append(team(players[1], players[3]))

    # Override for the toString method
    def __str__(self):
        output = ''
        for i, team in enumerate(self.teams):
            output += 'Team ' + str(i+1) + '\n'
            for player in team.members:
                output += player.__str__() + '\n'
            output += '\n'

        output += 'Kitty\n'
        for card in self.kitty:
            output += card.__str__() + ' '

        return output
