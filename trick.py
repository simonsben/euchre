# Class definition for tricks
class trick:
    def __init__(self):
        self.cards = []
        self.highest = None
        self.lead = None

    # Adds card to trick as players play
    def add_card(self, card_played, trump):
        self.cards.append(card_played)  # Adds card to trick

        if self.highest == None:    # If its the lead
            self.highest = card_played
            self.lead = card_played.suit
        elif self.highest.is_bigger(card_played, trump, self.lead):    # If the new card is bigger
            self.highest = card_played

    # Return the winner of the trick
    def get_winner(self):
        return self.cards.index(self.highest)
