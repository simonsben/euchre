from utilities import rank_lookup, suit_lookup

class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.index = -1

    def isSmaller(self, other_card):
        if self.suit == other_card.suit:
            return self.rank

    def __str__(self):
        suit = self.suit
        rank = rank_lookup.get(self.rank)
        index = self.index

        return suit_lookup.get(suit) + ' ' + rank + ' '  + str(index)
        # print('Suit', suit, 'Rank', rank, 'index', index)
