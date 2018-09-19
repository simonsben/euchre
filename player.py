from utilities import isLegal

class player:
    def __init__(self, id, name):
        self.id = id
        self.hand = []
        self.name = name

    def add_card(self, card):
        self.hand.append(card)
        if len(self.hand) > 5:
            print('Mans has more than 5 cards!')

    # Determine which cards can be played for this trick
    def trickOptions(self, trump):
        options = []
        for card in self.hand:
            if isLegal(trump, card):
                options.append(card)

        return options

    def __str__(self):
        output = self.name
        if len(self.hand) == 0:
            output += ' has no cards'
        else:
            for card in self.hand:
                output += ' '  + card.__str__()

        return output
