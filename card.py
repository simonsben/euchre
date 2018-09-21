from utilities import rank_lookup, suit_lookup, suit_pair

class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.index = -1

    def get_trump_rank(self,  trump):
        if self.rank == 2:
            if self.suit == trump: return 7
            return 6
        return self.rank

    def is_bigger(self, other_card, trump, lead):
        self_trump = self.is_trump(trump)
        other_trump =  other_card.is_trump(trump)

        if self_trump or other_trump:   # If one of the cards is trump
            if self_trump and not other_trump: return True  # If only self is trump
            elif not self_trump and other_trump: return False   # If only the other is trump

            # Both cards are trump
            self_rank = self.get_trump_rank(trump)
            other_rank = other_card.get_trump_rank(trump)
            return self_rank > other_rank

        elif self.suit == lead and other_card.suit != lead: return True     # Other is off-suit non-trump
        elif self.suit != lead and other_card.suit == lead: return False    # Self is off-suit non-trump
        return self.rank > other_card.rank  # Both are lead suit


    def is_trump(self, trump):
        if self.suit == trump: return True
        elif self.rank == 2 and self.suit == suit_pair.get(trump): return True

        return False

    def is_legal(self, trump, lead):
        if lead == trump:   # If its trump
            if self.is_trump(trump): return True
            return False

        elif self.suit == lead: # Non-trump
            if self.rank != 2: return True  # Non-Jack
            return trump != suit_pair.get(self.suit)    # Jack

        return False    # Not same suit

    def __str__(self):
        suit = self.suit
        rank = rank_lookup.get(self.rank)
        index = self.index

        return suit_lookup.get(suit) + ' ' + rank + ' '  + str(index)
        # print('Suit', suit, 'Rank', rank, 'index', index)
