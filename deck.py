from utilities import suits, ranks
from card import card
from random import random


class deck:
    def __init__(self):
        self.fill_deck()
        self.shuffle()


    def fill_deck(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(card(suit, rank))

    def shuffle(self):
        for card in self.cards:     # Assign random value to each card
            card.index = random()
        self.sort_deck()    # Order the cards based on the random values

        for i, card in enumerate(self.cards):   # Re-number the deck indexes
            card.index = i

    def sort_deck(self):
        for i,_ in enumerate(self.cards):
            min = i
            for j in range(i, len(self.cards)):
                if self.cards[min].index > self.cards[j].index:
                    min = j

            if min != i:
                hold = self.cards[min]
                self.cards[min] = self.cards[i]
                self.cards[i] = hold

    def __str__(self):
        output = ''
        for i, card in enumerate(self.cards):
            output += str(i+1) + ' ' + card.__str__() + '\n'

        return output
