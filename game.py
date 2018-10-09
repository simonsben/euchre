from utilities import random_number, get_player, \
    sample_players, ask_order_up, ask_other_suits, suits
from deck import deck
from player import player
from team import team
from copy import deepcopy

# NOTE:
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

        self.play_game()

    # Play game
    def play_game(self):
        # print(self)
        while not self.trump:
            self.choose_trump()
            if self.trump:
                print('Trump chosen', self.trump)
            else:
                print('Trump not chosen, re-dealing..')


    # Choose trump for the hand
    def choose_trump(self):
        print('Card up is', self.kitty[0]) # Show flipped card

        # Initialize prompt to user
        prompt = 'Do you want to order up ' + \
                 self.players[self.dealer].name + '? (y/n)'

        # Check if players want to order up dealer
        order_up = ask_order_up(prompt, self.players)

        if order_up != -1: # If dealer is ordered up
            self.trump = self.kitty[0].suit # Set suit for hand
            return

        # If dealer wasn't ordered up
        no_go_suit = self.kitty[0].suit # Suit that can't be chosen
        suit_options = deepcopy(suits)  # All suits
        suit_options.remove(no_go_suit)        # Remove no-go suit
        prompt = 'Would you like to call anything except ' + no_go_suit

        # Check if players want to call
        suit_choice = ask_other_suits(prompt, suit_options, self.players)

        if suit_choice == 'p':  # If everyone passed
            self.re_deal()
            return
        self.trump = suit_choice



    # Re-deal deck (if no suit is chosen)
    def re_deal(self):
        self.dealer = get_player(self.dealer + 1)
        for player in self.players:
            player.clearHand()

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
