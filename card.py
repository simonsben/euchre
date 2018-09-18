

class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def isSmaller(self, other_card):
        if self.suit == other_card.suit:
            return self.rank
