from utilities import random_number, get_player, get_input, \
    sample_players, ask_order_up, ask_other_suits, suits
from deck import deck
from player import player
from team import team
from copy import deepcopy
from trick import trick


# NOTE:
# Players are indexed from 0 to 3, going clockwise

class game:
    def __init__(self):  # Initialize a new game
        dealer_id = random_number(3)  # Choose random first dealer
        self.dealer = dealer_id  # Assign the dealer ID

        self.gen_players()  # Generate players
        self.deck = deck()  # Generate the deck

        self.kitty = []  # Initialize the kitty
        self.hands = []  # Initialize hands
        self.trump = None  # Initialize trump
        self.alone = -1 # Initialize whether someone is alone
        self.caller = None # Initialize person who called trump

        self.make_teams()  # Split players into teams
        self.deal_cards()  # Divide cards between players

        self.play_game()  # Start game

    # Play game
    def play_game(self):
        game_over = False  # Initialize game over check

        while not game_over:  # Keep playing until one team wins
            # Choose trump
            while not self.trump:
                self.choose_trump()
                if self.trump:
                    print('Trump chosen', self.trump, 'alone:', self.alone)
                else:
                    print('Trump not chosen, re-dealing..')

            # Play hand
            game_over = self.play_hand()
            if game_over:  # Check if game is done
                print('Game over!')
                break

            self.re_deal()  # Re-deal the deck

    # Choose trump for the hand
    def choose_trump(self):
        print('Card up is', self.kitty[0])  # Show flipped card

        # Initialize prompt to user
        prompt = 'Do you want to order up ' + \
                 self.players[self.dealer].name + '? (y/n)'

        # Check if players want to order up dealer
        order_up, going_alone, caller = ask_order_up(prompt, self.players, self.dealer + 1)
        partner_is_dealer = (caller.id + 2) % 4 == self.dealer

        if order_up != -1:  # If dealer is ordered up
            self.trump = self.kitty[0].suit  # Set suit for hand
            self.alone = going_alone or partner_is_dealer
            self.caller = caller
            return

        # If dealer wasn't ordered up
        no_go_suit = self.kitty[0].suit  # Suit that can't be chosen
        suit_options = deepcopy(suits)  # All suits
        suit_options.remove(no_go_suit)  # Remove no-go suit
        prompt = 'Would you like to call anything except ' + no_go_suit

        # Check if players want to call
        suit_choice, going_alone, caller = ask_other_suits(prompt, suit_options, self.players, self.dealer + 1)

        if suit_choice == 'p':  # If everyone passed
            self.re_deal()
            return
        self.trump = suit_choice  # Set trump for hand
        self.alone = going_alone
        self.caller = caller

    def play_hand(self):
        leader = self.dealer + 1  # Track who has the lead
        for i in range(5):  # For each trick in the hand
            leader = self.play_trick(leader)

        print('\nHand done\n')

        # Total tricks and check if team has won
        zero_over, zero_win = self.teams[0].hand_over(self.alone, self.caller)
        one_over, one_win = self.teams[1].hand_over(self.alone, self.caller)

        print('Team zero won\n') if zero_win else print('Team one won\n')

        return zero_over or one_over

    def play_trick(self, leader):
        current_trick = trick()  # Initialize trick
        skip_player = -1
        if self.alone:
            skip_player = get_player(self.caller.id + 2)

        for i in range(leader, leader + 4):  # For each player after dealer
            if get_player(i) == skip_player:
                continue
            player = self.players[get_player(i)]  # Given player

            print(player.name + ' is up, cards are: ')
            num_cards = player.list_cards(self.trump, current_trick.lead)

            prompt = 'Choose card to play'
            card_index = get_input(prompt, list(range(num_cards)))
            card_played = player.hand[card_index]

            print('\n' + player.name + ' played ' + str(card_played) + '\n')

            current_trick.add_card(card_played, self.trump)  # Add card to trick
            player.playCard(card_played)  # Remove card from hand

        card_index = current_trick.get_winner()  # Index of card in trick
        player_id = (card_index - (leader + 1)) % 4  # Get player id from play index

        player = self.players[player_id]  # Player with winning card

        # Get winning team
        team_zero_win = self.teams[0].is_on_team(player)  # Check if team 0 won
        win_team_index = 0
        if team_zero_win: win_team_index = 1

        winning_team = self.teams[win_team_index]
        winning_team.add_trick(current_trick)  # Give winning team the trick

        print('\nTeam ' + str(win_team_index) + ' won the trick \n')

        return player_id

    # Re-deal deck (if no suit is chosen)
    def re_deal(self):
        self.dealer = get_player(self.dealer + 1)
        self.trump = None
        for player in self.players:
            player.clearHand()
        self.deck.shuffle()
        self.deal_cards()

    # Divide cards between players
    def deal_cards(self):
        for i, card in enumerate(self.deck.cards):
            if i >= 20:
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
            output += 'Team ' + str(i + 1) + '\n'
            for player in team.members:
                output += player.__str__() + '\n'
            output += '\n'

        output += 'Kitty\n'
        for card in self.kitty:
            output += card.__str__() + ' '

        return output
