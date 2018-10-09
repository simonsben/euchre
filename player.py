# Class to define player
class player:
    def __init__(self, id, name):
        self.id = id
        self.hand = []
        self.name = name

    # Adds a card to the players hand
    def add_card(self, card):
        self.hand.append(card)

        if len(self.hand) > 5:
            print('Mans has more than 5 cards!')

    # Determine which cards can be played for this trick
    def trickOptions(self, trump, lead):
        options = []
        for card in self.hand:  # Check each card
            if card.is_legal(trump, lead):  # Check if card can be played
                options.append(card)

        if len(options) == 0:  # If player doesn't have the suit lead
            options = self.hand

        return options

    # Return given card
    def playCard(self, card):
        self.hand.remove(card)

    # Clear hand for re-deal
    def clearHand(self):
        self.hand = []

    def list_cards(self, trump, lead):
        for i, card in enumerate(self.trickOptions(trump, lead)):
            print(str(i) + ': ' + str(card))

        return len(self.hand)

    # New to string method
    def __str__(self):
        output = self.name + ': '
        if len(self.hand) == 0:
            output += ' has no cards'
        else:
            for card in self.hand:
                output += card.__str__() + ' '

        return output + '\n'
