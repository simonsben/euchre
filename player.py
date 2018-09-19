

class player:
    def __init__(self, id, name):
        self.id = id
        self.hand = []
        self.name = name

    def add_card(self, card):
        self.hand.append(card)
        if len(self.hand) > 5:
            print('Mans has more than 5 cards!')

    def __str__(self):
        output = self.name
        if len(self.hand) == 0:
            output += ' has no cards'
        else:
            for card in self.hand:
                output += ' '  + card.__str__()

        return output
